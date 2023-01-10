!> @file hvy_calc_alpha.f90
!! @brief Calculate alpha = x^p.D(x).dt/dx^2 across the mesh
!!
!!

module calc_alpha_mod

    use kindtypes_mod, only: dp

    implicit none

    private
    public calc_alpha

    contains

    subroutine calc_alpha(ncells, geom, dt_by_dx2, cellpos, dcoeff, alpha)

        integer,  intent(in)                     :: ncells
        integer,  intent(in)                     :: geom
        real(dp), intent(in)                     :: dt_by_dx2
        real(dp), intent(in),  dimension(ncells) :: cellpos
        real(dp), intent(in),  dimension(ncells) :: dcoeff
        real(dp), intent(out), dimension(ncells) :: alpha

        integer :: icell

        write(*,*)
        write(*,*) "Calculating alpha..."
        write(*,*) "===================="

        write(*,*)
        write(*,*) "alpha(x) = x^p D(x) dt"
        write(*,*) "           -----------"
        write(*,*) "               dx^2   "

        write(*,*)
        do icell = 1,ncells

!            alpha(icell) = cellpos(icell)**geom * dcoeff(icell) * dt_by_dx2
            alpha(icell) = dcoeff(icell) * dt_by_dx2

        enddo

    end subroutine

end module
