module Gsselm_mod



implicit none
   !INTEGER, parameter :: dbp = SELECTED_REAL_KIND (15,307)
   INTEGER, parameter :: dbp = 8
   REAL(kind=8)  :: EPS, M_PI
   PARAMETER (EPS=3.0d-15)       	!EPS is the relative precision
   PARAMETER (M_PI=3.141592654d0)      ! Pi value

  contains

function Gsselm(a,row)
	INTEGER, INTENT(IN) :: row
	REAL(kind=8) , INTENT(INOUT)   ::  a(:,:)   	!Assume shape (:)
	REAL(kind=8) , DIMENSION(row) :: Gsselm

	INTEGER i,j,k
	INTEGER, DIMENSION(2) :: shap
	REAL(kind=8) , ALLOCATABLE :: swap_ik(:)
	REAL(kind=8)  :: tmp

	ALLOCATE (swap_ik(row+1))

! 	Initialise
	swap_ik(:) = 0.0d0            ! Whole vector initialized to zero
	tmp = 0.0d0

! Check dimensions of input matrix
	shap = SHAPE(a)
	if ( (shap(1) .NE. row) .OR.  (shap(2) .NE. row+1) ) then
   	return
	end if


!/*   Gaussian Elimination - Row Reduction of matrix  */
	do k=1, row-1                             ! total of row-1 operations

!/*  Pivotal strategy - SWAP rows to make pivotal element a[k][k] have the
!    greatest magnitude in its column. This prevents unnecessary division by
!    a small number.                           */
   	do i = k+1, row
      	if ( (dabs(a(i,k))-dabs(a(k,k))).gt.EPS  ) then
         	do j = k, row+1                     !/* If pivotal element is not */
            	swap_ik(j) = a(k,j)              !/* the highest then  */
          	   a(k,j) = a(i,j)                  !/* swap i'th and k'th rows */
            	a(i,j) = swap_ik(j)
         	end do 		!j-loop
         end if
   	end do 				!i-loop


!/*   If the Matrix is SINGULAR then EXIT program      */
  		IF ( dabs(a(k,k)) < EPS ) then
   		print *,'After swapping rows to make the pivotal element become the'
      	print *,'highest magnitude element in its column, its magnitude is'
	      print *,'still extremely small.'
	      print *,'Hence this is a SINGULAR MATRIX - no unique solution or '
	      print *,'check that the input dimensions are correct.'
!   	   call break()
	   END if



!/*      Perform row-reduction with pivotal element a[k][k]     */
		do i = k+1, row
			do j = row+1, k, -1			!/* starting from end of column */
	     	 	a(i,j) = a(i,j) - a(k,j) / a(k,k) * a(i,k)
			end DO 							!/* end of j loop     */
		end do 	 							!/* end of 2nd i loop */

	end DO 									!/* end of k loop     */
!  At this point, the bottom triangle is Zero


!/*   Back Substitution - Solutions of equations   */
	Gsselm(row) = a(row,row+1) / a(row,row)
	do k = row-1, 1, -1
   	tmp = 0.0d0
   	do j = k+1, row
      	tmp = tmp + a(k,j)*Gsselm(j)
	   end do 							!j-loop
   	Gsselm(k) = ( a(k,row+1) - tmp ) / a(k,k)
	end do 								!k-loop

   deallocate (swap_ik)
	RETURN
END function Gsselm

end module
