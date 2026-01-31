!> @file
!! @brief Calcuate mesh-based quantities (currently just diffusion coefficient)
!!
!!

module setup_mesh_mod

    implicit none

    contains


    subroutine setup_mesh(ncells, nmats, nregs, dx, nodepos, reg_bound, reg_matnum, reg_dcoeff, dcoeff)

        integer,      intent(in)                       :: ncells
        integer,      intent(in)                       :: nmats
        integer,      intent(in)                       :: nregs
        real(kind=8), intent(in)                       :: dx
        real(kind=8), intent(in),  dimension(ncells+1) :: nodepos    ! The position of each cell boundary
        real(kind=8), intent(in),  dimension(nregs)    :: reg_bound  ! The right-hand/outer boundary of each region
        integer,      intent(in),  dimension(nregs)    :: reg_matnum ! The material number of the material comprising each region
        real(kind=8), intent(in),  dimension(nregs)    :: reg_dcoeff ! The diffusion coeff of the material comprising each region
        real(kind=8), intent(out), dimension(ncells)   :: dcoeff     ! The diffusion coefficient of each cell

        real(kind=8) :: dleft, dright

        integer :: icell, ireg

        ireg = 1

        do icell = 1, ncells

            ! Whole cell is inside this region

            if (nodepos(icell+1) <= reg_bound(ireg)) then

                dcoeff(icell) = reg_dcoeff(ireg)

            ! Cell is not fully inside this region

            else

                dleft  = reg_bound(ireg) - nodepos(icell) ! The extent inside this region
                dright = dx - dleft                       ! The remainder in the next region

                ! Use a weighted average of the two regional diffusion coefficients for this cell

                if (ireg >= nregs) then
                    write(*,*) 'Error: cell spans beyond final region in setup_mesh'
                    stop 'Terminated by setup_mesh'
                endif

                dcoeff(icell) = (dleft*reg_dcoeff(ireg) + dright*reg_dcoeff(ireg+1))/dx
                ireg = ireg + 1

            endif

        enddo

    end subroutine

end module
