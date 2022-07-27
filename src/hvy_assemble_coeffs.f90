!! @brief Assemble the coefficient vectors: a, b and c
!!
!!

module assemble_coeffs_mod

    use kindtypes_mod, only: dp

    implicit none

    contains

    subroutine assemble_coeffs(ncells, geom, theta, nodepos, alpha, a, b, c)

        integer,  intent(in)          :: ncells
        integer,  intent(in)          :: geom
        real(dp), intent(in)          :: theta
        real(dp), dimension(ncells+1) :: nodepos
        real(dp), dimension(ncells)   :: alpha
        real(dp), dimension(ncells)   :: a, b, c

        integer :: j

        !write(*,*)
        !write(*,*) "Assembling coefficients..."
        !write(*,*) "=========================="


        ! These should never be needed (NOT TRUE, IN IMPLICIT SCHEME WITH NEUMANN BOUNDARY CONDITION ON LHS)
        j = 1
        a(j) = theta*alpha(j)
        b(j) = theta*(alpha(j) + alpha(j)) + 1._dp ! nodepos(j)**geom
        c(j) = theta*alpha(j)

        do j = 2, ncells
            a(j) = theta*alpha(j)
            b(j) = theta*(alpha(j) + alpha(j-1)) + 1._dp ! nodepos(j)**geom
            c(j) = theta*alpha(j-1)
        enddo

        ! Should never be needed (NOT TRUE, IN IMPLICIT SCHEME WITH NEUMANN BOUNDARY CONDITION ON RHS)
        j = ncells + 1
        a(j) = theta*alpha(j-1)                        ! For j = J, i.e. the outermost node, we need a ghost cell
        b(j) = theta*(alpha(j-1) + alpha(j-1)) + 1._dp ! on the exterior, for which we assume alpha(J) = alpha(J-1)
        c(j) = theta*alpha(j-1)

!        write(*,*)
!        do j = 1,ncells+1
!            write(*,*) j, a(j), b(j), c(j)
!        enddo

    end subroutine

end module
