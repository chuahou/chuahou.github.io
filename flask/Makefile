#################
### variables ###
#################

# system programs
CD    ?= cd
CP    ?= cp
ECHO  ?= echo
MKDIR ?= mkdir
RM    ?= rm

# directories
VENV_DIR       := venv
BUILD_DIR      := build
CSS_DIR        := inline/css
CSS_TARGET_DIR := templates/cssmin
TARGET_DIR     := ..

# programs
PIP        ?= $(VENV_DIR)/bin/pip3
PYTHON     ?= $(VENV_DIR)/bin/python3
SYS_PYTHON ?= python3
UGLIFYCSS  ?= uglifycss

# paths
CSS_SOURCE      := $(wildcard $(CSS_DIR)/*.css)
CSS_MIN         := $(CSS_SOURCE:$(CSS_DIR)/%.css=$(CSS_TARGET_DIR)/%.css)
FLASK_APP       := app.py
PIP_REQUIRE     := requirements.txt
STATIC_PRECIOUS := precious.txt # file of paths in target NOT to delete

# Matches all generated static content in the TARGET_DIR. All files already in
# TARGET_DIR that are not generated should be in STATIC_PRECIOUS (e.g. this
# directory's path, README, LICENCE etc) to not be included here
STATIC_CONTENT := $(shell find $(TARGET_DIR) \( `cat $(STATIC_PRECIOUS) | xargs printf "$(TARGET_DIR)/%s\n" | awk 'NR > 1 { printf("-o ") } { printf("-path %s ", $$1) }'` \) -prune -o -type f -print)

.PHONY: all clean run requirements minimize

# for coloured text
TPUT_YELLOW  := tput setaf 3
TPUT_DEFAULT := tput sgr0

####################
### main targets ###
####################

all: $(VENV_DIR) requirements minimize
	@$(TPUT_YELLOW)
	@$(ECHO) "Removing installed contents of $(TARGET_DIR)/ ..."
	@$(TPUT_DEFAULT)
	@$(RM) $(STATIC_CONTENT) || true
	@$(ECHO)

	@$(TPUT_YELLOW)
	@$(ECHO) "Using Frozen-Flask to build static site; ..."
	@$(TPUT_DEFAULT)
	@$(PYTHON) $(FLASK_APP)

	@$(TPUT_YELLOW)
	@$(ECHO) "Removing minimized CSS ..."
	@$(TPUT_DEFAULT)
	@$(RM) $(CSS_MIN)
	@$(ECHO)

	@$(TPUT_YELLOW)
	@$(ECHO) "Copying contents of $(BUILD_DIR)/ to $(TARGET_DIR)/ ..."
	@$(TPUT_DEFAULT)
	@$(CP) -r $(BUILD_DIR)/* $(TARGET_DIR)
	@$(ECHO)

clean:
	@$(TPUT_YELLOW)
	@$(ECHO) "Removing $(BUILD_DIR)/ ..."
	@$(TPUT_DEFAULT)
	@$(RM) $(BUILD_DIR) -rf || true
	@$(ECHO)

run:
	@$(TPUT_YELLOW)
	@$(ECHO) "Running HTTP server in $(TARGET_DIR)/ ..."
	@$(TPUT_DEFAULT)
	@$(CD) $(TARGET_DIR) && $(SYS_PYTHON) -m http.server
	@$(ECHO)

#######################
### pip requisities ###
#######################

$(VENV_DIR):
	@$(TPUT_YELLOW)
	@$(ECHO) "Creating virtual environment in $@ ..."
	@$(TPUT_DEFAULT)
	$(SYS_PYTHON) -m venv $@

requirements: $(VENV_DIR)
	@$(TPUT_YELLOW)
	@$(ECHO) "Installing requirements ..."
	@$(TPUT_DEFAULT)
	@$(PIP) install -r $(PIP_REQUIRE)
	@$(ECHO)

######################
### css mimization ###
######################

minimize: $(CSS_MIN)
	@$(TPUT_YELLOW)
	@$(ECHO) "Minimized CSS ..."
	@$(TPUT_DEFAULT)
	@$(ECHO)

$(CSS_TARGET_DIR):
	@$(MKDIR) -p $@

$(CSS_TARGET_DIR)/%.css: $(CSS_DIR)/%.css $(CSS_TARGET_DIR)
	@$(UGLIFYCSS) $< --output $@
