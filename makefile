# 
#            --------------------------------------------------
#                           Mouse Payload Loader                
#            --------------------------------------------------
#          Copyright (C) <2015>  <Entynetproject (Ivan Nikolsky)>
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        any later version.
#
#        This program is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#        GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#    About Author :   
#    Founder   : Entynetproject (Ivan Nikolsky)
#    Site      : http://entynetproject.simplesite.com/
#    Instagram : @entynetproject 
#    Twitter   : @entynetproject
#    Email     : entynetproject@gmail.com
#

ios:
	cd src/mplios;\
	rm -rf packages;\
	make clean;\
	make package -i;\
	dpkg -x packages/* new;\
	mv new/usr/bin/mplios ../../resources/mplios

mpl:
	cd src/mpl;\
	rm -rf packages;\
	make clean;\
	make package;\
	make -f Makefile --no-keep-going COLOR=1 --no-print-directory internal-tweak-all _THEOS_CURRENT_TYPE="tweak" THEOS_CURRENT_INSTANCE="mpl" _THEOS_CURRENT_OPERATION="all" THEOS_BUILD_DIR=".";\
	dpkg -x packages/* new;\
	mv new/Library/MobileSubstrate/DynamicLibraries/* ../../resources/;\
	rm -rf new

macos:
	cd src/mplmacos;\
	rm build/Release/mplmacos 2>/dev/null;\
	xcodebuild -target mplmacos -configuration Release;\
	rm ../../resources/mplmacos;\
	mv build/Release/mplmacos ../../resources/mplmacos

all: ios macos mpl 
