include /Users/Enty8080/theos/makefiles/common.mk
# sudo xcode-select /Applications/xcode7.2.1.app
TWEAK_NAME = Mouse
mpl_FILES = Tweak.xm
mpl_PRIVATE_FRAMEWORKS = AppSupport
include /Users/Enty8080/theos/makefiles/tweak.mk

after-install::
	install.exec "killall -9 SpringBoard"
