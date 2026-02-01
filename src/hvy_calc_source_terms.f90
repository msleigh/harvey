!> @file
!! @brief Calculate the source term, Q, across the mesh (not currently used)
!!
!!

module calc_source_terms_mod

   use kindtypes_mod, only: dp

   implicit none

   contains

   subroutine calc_source_terms(ncells, src)

      integer, intent(in)                     :: ncells
      real(dp), intent(out), dimension(ncells) :: src

      integer :: icell

      write(*,*)
      write(*,*) "Calculating source term..."
      write(*,*) "=========================="


      ! Placeholder source term: fill with a sentinel until a physical source is defined.
      ! Keeping a distinct large negative value makes it obvious if this stub is used.
      src(:) = -32767._dp

!      write(*,*)
!      do icell = 1,ncells
!        write(*,*) icell, src(icell)
!      enddo

   end subroutine

end module
