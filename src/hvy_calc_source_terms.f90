!> @file  
!! @brief Calculate the source term, Q, across the mesh (not currently used)
!!
!! 

module calc_source_terms_mod

   implicit none
   
   contains
   
   subroutine calc_source_terms(ncells, src)
   
      integer,      intent(in)                     :: ncells 
      real(kind=8), intent(out), dimension(ncells) :: src
      
      integer :: icell
      
      write(*,*)
      write(*,*) "Calculating source term..."
      write(*,*) "=========================="
      
      
      ! Should not be needed yet
      src(:) = -32767.
      
!      write(*,*)
!      do icell = 1,ncells
!        write(*,*) icell, src(icell)
!      enddo
      
   end subroutine

end module
