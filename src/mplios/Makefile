include $(THEOS)/makefiles/common.mk
export SYSROOT = /opt/theos/sdks/iPhoneOS9.3.sdk
export TARGET_CODESIGN_FLAGS="-Ssign.plist"
TOOL_NAME = mplios

mplios_FILES = main.mm mpl.m
mplios_OBJ_FILES = libcrypto.a libssl.a
mplios_FRAMEWORKS = Foundation Security AudioToolbox CoreFoundation AVFoundation MediaPlayer UIKit
mplios_PRIVATE_FRAMEWORKS = AppSupport SpringBoardServices IOSurface

include $(THEOS_MAKE_PATH)/tool.mk

export ARCHS = armv7 arm64

CFLAGS = -Wall -g
