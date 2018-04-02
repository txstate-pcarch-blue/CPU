#!/bin/bash
pushd $(dirname "${0}") > /dev/null
ROOTD=$(pwd -L)
echo "$ROOTD"
pushd "$ROOTD/lib" > /dev/null

echo Downloading myhdl library
git submodule update
if [ ! -d "myhdl" ]; then
   echo Error: Unable to download myhdl
   exit
fi
cd myhdl/cosimulation/icarus

echo Building myhdl.vpi
make
if [ ! -f "myhdl.vpi" ]; then
   echo Error: Unable to build myhdl.vpi
   exit
fi

echo Copying myhdl.bpi to bin
cp myhdl.vpi "$ROOTD/bin/myhdl.vpi"
if [ ! -f "$ROOTD/bin/myhdl.vpi" ]; then
   echo Error: Unable to copy myhdl.vpi to bin
   exit
fi
echo myhdl.bpi created at "$ROOTD/bin/myhdl.vpi"

# Return to the original directory
popd > /dev/null
popd > /dev/null
