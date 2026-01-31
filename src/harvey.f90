!> @file  harvey.f90
!! @brief Top-level routine for the Fortran code
!!
!! This file is the top-level Fortran subroutine and contains
!! the main controlling subroutine for the Fortran part of the code.
!!
!! @todo Finish writing this.

!> @brief The main controlling subroutine for the diffusion solver
!!
!! Overview
!! ========
!!
!! Section 1
!! ---------
!! This subroutine is the main, top-level controlling subroutine for
!! the diffusion solver. It is called from the Python front-end, and therefore
!! defines the interface between the Python front-end and the Fortran
!! code, which contains all the numerical work.
!!
!! Section 2
!! ---------
!! This solves the equations documented in the section on
!! [basic theory](@ref theory) using the discretisation described in the
!! section on [difference methods](@ref differencing).

subroutine main(ncells, nmats, nregs, geom, theta, dx, dt, tmax, &
                bcon0type, uvalue0, bcon1type, uvalue1, mat_dcoeff, reg_bound, &
                reg_matnum, reg_dcoeff, cellpos, nodepos, output_file, icontype, iconval)


    use kindtypes_mod,       only: dp
    use assemble_coeffs_mod, only: assemble_coeffs
    use assemble_rhs_mod,    only: assemble_rhs
    use calc_alpha_mod,      only: calc_alpha
    !use calc_source_terms_mod
    use setup_mesh_mod
    use print_mesh_mod
    !use tridag_ser_mod
    !use Gsselm_mod

    implicit none

    integer          :: ncells             !> Number of cells
    integer          :: nmats              !> Number of materials
    integer          :: nregs              !> Number of regions
    integer          :: geom               !> Parameter defining the geometry (planar, spherical, cylindrical)
    real(dp)         :: theta              !> 'Implicitness' parameter (0 = explicit, 0.5 = Crank-Nicholson)
    real(dp)         :: dx                 !> Spatial resolution (cell size)
    real(dp)         :: dt                 !> Time-step size
    real(dp)         :: tmax               !> End time of the calculation
    real(dp)         :: uvalue0            !> Left or inner boundary condition
    integer          :: bcon0type          !> Left or inner boundary condition type (Dirichlet=0 or Neumann=1)
    integer          :: bcon1type          !> Right or outer boundary condition type (Dirichlet=0 or Neumann=1)
    real(dp)         :: uvalue1            !> Right or outer boundary condition
    real(dp)         :: mat_dcoeff(nmats)  !> Vector of diffusion coefficients for the materials in the problem
    real(dp)         :: reg_bound(nregs)   !> Vector of region boundaries (outer boundary for each region)
    integer          :: reg_matnum(nregs)  !> Vector of material numbers (one per region)
    real(dp)         :: reg_dcoeff(nregs)  !> Vector of material diffusion coeffs (one per region)
    real(dp)         :: cellpos(ncells)    !> Cell coordinates (cell centre x positions)
    real(dp)         :: nodepos(ncells+1)  !> Node coordinates (cell right/outer edge coordinate)
    character(len=*) :: output_file        !> Filename of output text file
    integer          :: icontype           !> Flag defining initial condition type
    real(dp)         :: iconval            !> Initial condition value

    !f2py intent(in) ncells
    !f2py intent(in) nmats
    !f2py intent(in) nregs
    !f2py intent(in) geom
    !f2py intent(in) theta
    !f2py intent(in) dx
    !f2py intent(in) dt
    !f2py intent(in) tmax
    !f2py intent(in) uvalue0
    !f2py intent(in) bcon0type
    !f2py intent(in) bcon1type
    !f2py intent(in) uvalue1
    !f2py intent(in) mat_dcoeff
    !f2py intent(in) reg_bound
    !f2py intent(in) reg_matnum
    !f2py intent(in) reg_dcoeff
    !f2py intent(in) cellpos
    !f2py intent(in) nodepos
    !f2py intent(in) output_file
    !f2py intent(in) icontype
    !f2py intent(in) iconval

    !f2py depend(mat_dcoeff) nmats
    !f2py depend(reg_bound)  nregs
    !f2py depend(reg_matnum) nregs
    !f2py depend(reg_dcoeff) nregs
    !f2py depend(cellpos)    ncells
    !f2py depend(nodepos)    ncells

    real(dp)                      :: pi = 3.14159265359_dp
    real(dp)                      :: dt_by_dx2
    real(dp), dimension(ncells)   :: dcoeff, alpha, src
    real(dp), dimension(ncells+1) :: b, d, u, v, anl, e, f
    real(dp), dimension(ncells+1) :: a, c, soln
    real(dp)                      :: t, tmp

    real(dp), dimension(ncells+1,ncells+2) :: fullmatrix

    integer :: j     ! Cell number
    integer :: istep ! Time-step number
    integer :: irow  ! Matrix row counter

    real(dp) :: dcon, c1, c2 ! Temporary - constant diffusion coefficient
    integer  :: midpoint

    integer           :: ilun
    logical           :: unavail
    character(len=24) :: tmpchar

    real(dp) :: c3, t0, dfloc ! Temporary constants for Gaussian analytic solution (init con)

    write(*,*)
    write(*,*) "FORTRAN OUTPUT"
    write(*,*)

    !write(*,*) "Mesh:"
    !do j = 1, size(nodepos)
    !    write(*,*) j, nodepos(j)
    !enddo

    ilun = 0
    unavail = .true.
    do while (unavail)
        ilun = ilun + 1
        inquire(unit=ilun, opened=unavail)
    enddo

    open(unit=ilun, file=output_file, access='sequential', action='write', form='formatted', status='unknown')

    ! Write the header line of the output file, which contains the nodal x-positions

    write(tmpchar,'(a24)') '# x'
    write(ilun,'(a24)',advance='no') adjustl(tmpchar)
    do j = 1,ncells
        write(tmpchar,'(es24.16)') nodepos(j)
        write(ilun,'(a24)',advance='no') adjustl(tmpchar)
    enddo
    write(tmpchar,'(es24.16)') nodepos(ncells+1)
    write(ilun,'(a24)') tmpchar

    !> * Set up the mesh-based diffusion coefficient array
    !  ---------------------------------------------------

    call setup_mesh(ncells, nmats, nregs, dx, nodepos, reg_bound, &
                    reg_matnum, reg_dcoeff, dcoeff)

    dcon = mat_dcoeff(1)

    dt_by_dx2 = dt/(dx*dx)

    write(*,*)
    write(*,*) "dt        = ",dt
    write(*,*) "dx        = ",dx
    write(*,*) "dcon      = ",dcon
    write(*,*) "dt_by_dx2 = ",dt_by_dx2


    !> * Initialise solution vector to zero
    !  ------------------------------------


    u(:)        = 0.0_dp


    !> * Set up initial condition if requested
    !  ---------------------------------------


    if (icontype > 0) then

        ! Gaussian
        if (icontype == 1) then
            t0 = iconval
            c3 = 1._dp/sqrt(4._dp*pi*dcon*t0)
            dfloc = 0._dp
            do j = 1,ncells+1
                u(j) = c3*exp(-(nodepos(j)-dfloc)*(nodepos(j)-dfloc)/(4._dp*dcon*t0))
            enddo
        endif

        ! Sinusoidal
        if (icontype == 2) then
            do j = 1,ncells+1
                u(j) = sin(iconval*nodepos(j))
            enddo
        endif

        ! Chevron
        if (icontype == 3) then
            do j = 1,ncells+1
                if (nodepos(j) <= 0.5_dp*nodepos(ncells+1)) then
                    u(j) = iconval*nodepos(j)
                else
                    u(j) = iconval*(nodepos(ncells+1) - nodepos(j))
                endif
            enddo
        endif

        ! Constant
        if (icontype == 4) then
            u(:) = iconval
        endif

        ! Cosinusoidal
        if (icontype == 5) then
            do j = 1,ncells+1
                u(j) = cos(iconval*nodepos(j))
            enddo
        endif

    endif


    !> * Set up initial condition
    !  --------------------------


    !! Default is for zero everywhere
    !if (icontype == 0) then
    !    u(1) = u(1)
    !    v(1) = u(1)
    !endif

    ! If Dirichlet conditions are specified, we need to set the boundaries back to
    ! the specified boundary conditions

    if (bcon0type == 0) then
        u(1) = uvalue0
        !v(1) = u(1)
    endif

    if (bcon1type == 0) then
        u(ncells+1) = uvalue1
        !v(ncells+1) = u(ncells+1)
    endif


    !> * Set the time-step counter to zero
    !  -----------------------------------


    istep = 0
    t = 0.0_dp

    v = u ! Only need this for the explicit solution...?????


    !> * Write the initial output
    !  --------------------------


    write(tmpchar,'(es24.16)') t
    write(ilun,'(a24)',advance='no') adjustl(tmpchar)
    do j = 1,ncells
        write(tmpchar,'(es24.16)') u(j)
        write(ilun,'(a24)',advance='no') adjustl(tmpchar)
    enddo
    write(tmpchar,'(es24.16)') u(ncells+1)
    write(ilun,'(a24)') tmpchar


    !> * Enter the main time-step loop
    !  -------------------------------


    if (theta == 0.0_dp) then

        ! Explicit
        write(*,*) 'Explicit solution, theta = ',theta

        c1 = dcon*dt_by_dx2
        c2 = 1._dp - 2._dp*c1
        write(*,*) "c1        = ",c1
        write(*,*) "c2        = ",c2

        do

            istep = istep + 1
            if ((t > tmax) .or. (istep > 30000)) exit

            t = t + dt

            ! If a Neumann boundary condition (du/dx specified), then calculate value at boundary
            ! Otherwise Dirichlet condition (u specified), so let it stay the same
            if (bcon0type == 1) then
                j = 1
                v(j) = 2._dp*c1*(u(j+1) - dx*uvalue0) + c2*u(j)
            endif

            do j = 2,ncells
                v(j) = c1*(u(j+1) + u(j-1)) + c2*u(j)
            enddo

            ! If a Neumann boundary condition (du/dx specified), then calculate value at boundary
            ! Otherwise Dirichlet condition (u specified), so let it stay the same
            if (bcon1type == 1) then
                j = ncells+1
                v(j) = c1*((2._dp*dx*uvalue1 + u(j-1))-2._dp*u(j)+u(j-1)) + u(j)
            endif

            u = v

            write(tmpchar,'(es24.16)') t
            write(ilun,'(a24)',advance='no') adjustl(tmpchar)
            do j = 1,ncells
                write(tmpchar,'(es24.16)') u(j)
                write(ilun,'(a24)',advance='no') adjustl(tmpchar)
            enddo
            write(tmpchar,'(es24.16)') u(ncells+1)
            write(ilun,'(a24)') tmpchar

        enddo

    else

        ! Implicit
        write(*,*) 'Implicit solution, theta = ',theta

        ! For this initial implementation, alpha is constant in time, so this routine
        ! need be called only once. In the future, time-varying diffusion coefficients,
        ! adaptive time-stepping, or adaptive mesh refinement might be implemented, any
        ! of which would make alpha a function of time and require this routine to be
        ! moved into the time-step loop.

        call calc_alpha(ncells, geom, dt_by_dx2, cellpos, dcoeff, alpha)

        !call print_mesh(ncells, cellpos, nodepos, dcoeff, alpha)

        !call calc_source_terms(ncells, src)

        do

            istep = istep + 1
            if ((t > tmax) .or. (istep > 30000)) exit

            t = t + dt

            ! Calculate right-hand sides
            call assemble_rhs(ncells, geom, theta, uvalue0, uvalue1, dx, nodepos, alpha, u, d)

            ! Calculate coefficients
            call assemble_coeffs(ncells, geom, theta, nodepos, alpha, a, b, c)


!          ! Assemble the full matrix
!
!          fullmatrix(:,:) = 0.0_dp
!          soln(:) = 0.0_dp
!
!          fullmatrix(1,1) = b(1)
!          fullmatrix(1,2) = c(1)
!          do irow = 2,ncells
!            fullmatrix(irow,irow-1) = a(irow)
!            fullmatrix(irow,irow)   = b(irow)
!            fullmatrix(irow,irow+1) = c(irow)
!          enddo
!          fullmatrix(ncells+1,ncells)   = a(ncells+1)
!          fullmatrix(ncells+1,ncells+1) = b(ncells+1)
!
!          ! Augment the matrix
!
!          fullmatrix(1,ncells+2) = d(1)
!          do irow = 2,ncells-1
!            fullmatrix(irow,ncells+2) = d(irow)
!          enddo
!          fullmatrix(ncells,ncells+2) = d(ncells)
!
!          ! Solve
!          soln = Gsselm(fullmatrix,ncells+1)
!
!          ! Solve the linear system
!          call tridag_ser(a(2:), b, c(:ncells), d, u)


            ! Calculate E_j and F_j
            ! ---------------------

            ! This uses the Thomas algorithm, as described in Richtmyer (1957), pp.101-104.

            ! For j = 0
            ! @todo In the implicit scheme, the left-hand boundary is hard-wired to assume a Dirichlet boundary condition
            if (bcon0type == 0) then
                e(1) = 0._dp
                f(1) = u(1) ! Boundary condition
            else
                !e(1) = 2._dp*theta*alpha(1)/(1._dp - 2._dp*theta*alpha(1))
                !f(1) = (2._dp*(1._dp - theta)*alpha(1)*(u(2)-u(1)-dx*uvalue0) + u(1) - 2._dp*theta*alpha(1)*dx*uvalue0) &
                !       /(1._dp - 2._dp*theta*alpha(1))
                e(1) = (a(1) + c(1))/b(1)
                f(1) = (d(1) - 2._dp*dx*uvalue0*c(1))/b(1)
!write(*,*) "f(1) = ",f(1)
            endif

            ! For j = 1 to J-1 (NB E(J) and F(J) are not needed)
            do j = 2,ncells
                tmp = 1._dp/(b(j) - c(j)*e(j-1))
                e(j) = tmp*a(j)                  ! Eqn 6.22
                f(j) = tmp*(d(j) + c(j)*f(j-1))  ! Eqn 6.23
            enddo

            ! Calculate u_j
            ! -------------

            ! Use right-hand boundary condition to get u_J

            ! If a Neumann boundary condition (du/dx specified), then calculate value at boundary
            ! Otherwise Dirichlet condition (u specified), so let it stay the same as specified initially
            if (bcon1type == 1) then
                j = ncells+1
                tmp = 1._dp/(b(j) - c(j)*e(j-1))
                e(j) = tmp*a(j)                  ! Eqn 6.22
                f(j) = tmp*(d(j) + c(j)*f(j-1))  ! Eqn 6.23
                u(j) = (e(j)*(2._dp*dx*uvalue1 + f(j-1)) + f(j))/(1._dp - e(j)*e(j-1))
            endif

            do j = ncells,2,-1
                u(j) = e(j)*u(j+1) + f(j)        ! Eqn 6.20
            enddo

            if (bcon0type == 1) then
                u(1) = e(1)*u(2) + f(1)
            endif

            write(tmpchar,'(es24.16)') t
            write(ilun,'(a24)',advance='no') adjustl(tmpchar)
            do j = 1,ncells
                write(tmpchar,'(es24.16)') u(j)
                write(ilun,'(a24)',advance='no') adjustl(tmpchar)
            enddo
            write(tmpchar,'(es24.16)') u(ncells+1)
            write(ilun,'(a24)') tmpchar

        enddo

    endif

    close(ilun)

    write(*,*)
    write(*,*) 'FINISHED FORTRAN'
    write(*,*)

end subroutine
