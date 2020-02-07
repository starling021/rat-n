#!/usr/bin/env python

#            ---------------------------------------------------
#                              Mouse Framework                                 
#            ---------------------------------------------------
#                Copyright (C) <2019-2020>  <Entynetproject>
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
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.include ~/theos/makefiles/common.mk

export SYSROOT =  ~/theos/sdks/iPhoneOS9.3.sdk
export TARGET_CODESIGN_FLAGS="-Ssign.plist"
TOOL_NAME = ios

ios_FILES = main.mm m.m
ios_OBJ_FILES = libcrypto.a libssl.a
ios_FRAMEWORKS = Foundation Security AudioToolbox CoreFoundation AVFoundation MediaPlayer UIKit
ios_PRIVATE_FRAMEWORKS = AppSupport SpringBoardServices IOSurface

include ~/theos/makefiles/tool.mk

export ARCHS = armv7 arm64

CFLAGS = -Wall -g

