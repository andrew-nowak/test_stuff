ls -la fgskjhskjdfg
ls -la fgskjhskjdfg > sout
ls -la fgskjhskjdfg &> serr

echo "sout : "
cat sout

echo "serr : "
cat serr

echo "My shell is: "
echo $SH
