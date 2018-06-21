program ABINITband
integer :: nkpts, nbands, i, j
real :: efermi, conversion
real, allocatable :: res(:,:)
character(LEN=80) :: cline
character :: lspin
character*3 tmp

conversion = 27.2114
open(1, file='bands_xo_EIG', status='old')

print *, 'Enter the number of k-points'
read *, nkpts

print *, 'Enter the number of bands'
read *, nbands

print *, 'Enter the Fermi level (Hartree)'
read *, efermi

allocate(res(nkpts,nbands))

read(1,*) cline
do i = 1, nkpts
   read(1,*) cline
   read(1,*) res(i,:)
end do
do j = 1, nbands
  write(tmp, '(I3.3)') j
   open(2, file='band'//tmp//'.dat',status='replace')
   do i = 1, nkpts
      write(2,*) (res(i,j)-efermi)*conversion
   end do
   close(2)
end do

end program ABINITband
