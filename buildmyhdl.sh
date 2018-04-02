#!/bin/bash
pushd $(dirname "${0}") > /dev/null
BASED=$(pwd -L)
echo "Using $BASED as base directory"
pushd "$BASED/lib/myhdl" > /dev/null

echo Downloading myhdl library
git submodule init
git submodule update
if [ ! -d "cosimulation" ]; then
   echo Error: Unable to download myhdl
   exit
fi
cd "$BASED/lib/myhdl/cosimulation/icarus"

echo Building myhdl.vpi
make
if [ ! -f "myhdl.vpi" ]; then
   echo Error: Unable to build myhdl.vpi
   exit
fi

echo Copying myhdl.bpi to bin
cp myhdl.vpi "$BASED/bin/myhdl.vpi"
if [ ! -f "$BASED/bin/myhdl.vpi" ]; then
   echo Error: Unable to copy myhdl.vpi to bin
   exit
fi
echo myhdl.bpi created at "$BASED/bin/myhdl.vpi"

# Return to the original directory
popd > /dev/null
popd > /dev/null
