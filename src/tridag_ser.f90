!> @file
!! @brief Provides a generic serial routine to solve a tridiagonal matrix (from Numerical Recipes)
!!
!!

module tridag_ser_mod

interface assert_eq
    module procedure assert_eq
end interface

contains

function assert_eq(nn, string)


  implicit none

  character(len=*),      intent(in) :: string
  integer, dimension(:), intent(in) :: nn

  integer :: assert_eq

  if (all(nn(2:) == nn(1))) then
      assert_eq = nn(1)
  else
      write(*,*) 'Error: assert_eq failed with this tag: ', string
      stop 'Terminated by assert_eq'
  endif
end function assert_eq


subroutine myerror(string)
    character(len=*), intent(in) :: string
    write(*,*) 'Error: ',string
    stop 'Terminated by myerror'
end subroutine myerror


subroutine tridag_ser(a, b, c, r, u)

    implicit none

    real(kind=8), dimension(:), intent(in)  :: a, b, c, r
    real(kind=8), dimension(:), intent(out) :: u

    real(kind=8), dimension(size(b)) :: gam

    integer :: n, j
    real(kind=8) :: bet

    write(*,*) 'a', size(a)
    write(*,*) 'b', size(b)
    write(*,*) 'c', size(c)
    write(*,*) 'r', size(r)
    write(*,*) 'u', size(u)
    n = assert_eq((/size(a)+1, size(b), size(c)+1, size(r), size(u)/), 'tridag_ser')

    bet = b(1)

    if (bet == 0.0) call myerror('Re-write your equations as a set of order N-1, with u2 trivially eliminated')

    u(1) = r(1)/bet

    ! Decomposition and forward substitution

    do j = 2,n

        gam(j) = c(j-1)/bet

        bet = b(j) - a(j-1)*gam(j)

        if (bet == 0.0) call myerror('Stage 2 failure')

        u(j) = (r(j) - a(j-1)*u(j-1))/bet

    enddo

    ! Backsubstitution

    do j = n-1, 1, -1

        u(j) = u(j) - gam(j+1)*u(j+1)

    enddo

end subroutine tridag_ser

end module tridag_ser_mod
