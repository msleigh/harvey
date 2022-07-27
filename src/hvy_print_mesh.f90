!> @file
!! @brief Provides a subroutine to print the mesh coordinates and mesh-based quantities
!!
!!

module print_mesh_mod

   implicit none

   contains

   subroutine print_mesh(ncells, cellpos, nodepos, dcoeff, alpha)


      integer,      intent(in) :: ncells
      real(kind=8), intent(in) :: cellpos(ncells)
      real(kind=8), intent(in) :: nodepos(ncells+1)
      real(kind=8), intent(in) :: dcoeff(ncells)
      real(kind=8), intent(in) :: alpha(ncells)

      integer :: icell


      write(*,*)
      write(*,*) "Mesh..."
      write(*,*) "======="

      write(*,*)
      do icell = 1, ncells
         write(*,*) icell, nodepos(icell), cellpos(icell), nodepos(icell+1), dcoeff(icell), alpha(icell)
      enddo

   end subroutine print_mesh

end module
