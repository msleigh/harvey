!> @file
!! @brief Assemble the right-hand side: vector d
!!
!!

module assemble_rhs_mod

    use kindtypes_mod, only: dp

    implicit none

    contains

    subroutine assemble_rhs(ncells, geom, theta, uvalue0, uvalue1, dx, nodepos, alpha, u, d)

        integer,  intent(in)                       :: ncells
        integer,  intent(in)                       :: geom
        real(dp), intent(in)                       :: theta
        real(dp), intent(in)                       :: uvalue0
        real(dp), intent(in)                       :: uvalue1
        real(dp), intent(in)                       :: dx
        real(dp), intent(in),  dimension(ncells+1) :: nodepos
        real(dp), intent(in),  dimension(ncells)   :: alpha
        real(dp), intent(in),  dimension(ncells+1) :: u
        real(dp), intent(out), dimension(ncells+1) :: d

        integer :: j

        !write(*,*)
        !write(*,*) "Assembling right-hand side..."
        !write(*,*) "============================="


        ! -A_j u_{j+1} + B_j u_j - C_j u_{j-1} = b_j
        !
        !     where all quantities on the LHS are at time level (n+1)
        !           all quantities on the RHS are at time level (n)

        ! A_j = theta alpha_{j+1/2}
        ! B_j = theta (alpha_{j+1/2} + alpha_{j-1/2}) + x^p
        ! C_j = theta alpha_{j-1/2}

        ! b_j = (1 - theta)[alpha_{j+1/2}(u_{j+1} - u_j) - alpha_{j-1/2}(u_j - u_{j-1})] + x^p u_j

        ! alpha(x) = x^p D(x) dt / dx^2

        ! We should never need b_0, as E_0 and F_0 are calculated directly from the left-hand
        ! boundary condition.
        ! Left boundary (j=1) with Neumann BC du/dx = uvalue0:
        !   use ghost value u_0 = u_2 - 2*dx*uvalue0 so that (u_1 - u_0) matches the gradient.
        j = 1
!       d(j) = (1._dp-theta)*(alpha(j)*(u(j+1) - u(j)) - alpha(j-1)*(u(j) - u(j-1)                   )) + (nodepos(j)**geom)*u(j)
        d(j) = (1._dp-theta)*(alpha(j)*(u(j+1) - u(j)) - alpha(j)  *(u(j) - (u(j+1)-2._dp*dx*uvalue0))) + (nodepos(j)**geom)*u(j)
!write(*,*) "d(j) = ",d(j)

        do j = 2,ncells
            d(j) = (1._dp - theta)*(alpha(j)*(u(j+1) - u(j)) - alpha(j-1)*(u(j) - u(j-1))) + (nodepos(j)**geom)*u(j)
        enddo

        ! We should never need b_J, as we do not need E_J or F_J either - NOT TRUE FOR NEUMAN BOUNDARY IN IMPLICIT SCHEME.
        ! Right boundary (j=ncells+1) with Neumann BC du/dx = uvalue1:
        !   use ghost value u_{J+1} = u_{J-1} + 2*dx*uvalue1 for the outer gradient.
        j = ncells + 1
        d(j) = (1._dp-theta)*(alpha(j-1)*(2._dp*dx*uvalue1 + u(j-1) - u(j)) - alpha(j-1)*(u(j) - u(j-1))) + (nodepos(j)**geom)*u(j)

!        write(*,*)
!        do j = 1,ncells+1
!            write(*,*) j, d(j)
!        enddo

    end subroutine

end module
