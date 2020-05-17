# system programs
CD   := cd
CP   := cp
ECHO := echo
RM   := rm

# programs
PIP        := $(VENV)/bin/pip3
PYTHON     := $(VENV)/bin/python3
SYS_PYTHON := python3
VENV       := venv

# paths
BUILD_DIR       := build
TARGET_DIR      := ..
FLASK_APP       := app.py
PIP_REQUIRE     := requirements.txt
STATIC_PRECIOUS := precious.txt # file of paths in target NOT to delete

# matches all static content in the TARGET_DIR
STATIC_CONTENT = $(shell find $(TARGET_DIR) \( `cat $(STATIC_PRECIOUS) | xargs printf "../%s\n" | awk 'NR > 1 { printf("-o ") } { printf("-path %s ", $$1) }'` \) -prune -o -type f -print)

.PHONY: all build install uninstall clean run requirements

all: $(VENV) requirements
	@$(ECHO) "make build to build static to $(BUILD_DIR)/"
	@$(ECHO) "make install to copy static to $(TARGET_DIR)/"
	@$(ECHO) "make run to run static from $(TARGET_DIR)/"

$(VENV):
	@$(ECHO) "Creating virtual environment in $@..."
	$(SYS_PYTHON) -m venv $@

build:
	@$(ECHO) "Using Frozen-Flask to build static site;..."
	$(PYTHON) $(FLASK_APP)

install: uninstall
	@$(ECHO) "Copying contents of $(BUILD_DIR)/ to $(TARGET_DIR)/..."
	$(CP) -r $(BUILD_DIR)/* $(TARGET_DIR)

uninstall:
	@$(ECHO) "Removing installed contents of $(TARGET_DIR)/..."
	$(RM) $(STATIC_CONTENT) || true

clean:
	$(RM) $(BUILD_DIR) -rf

run:
	@$(ECHO) "Running HTTP server in $(TARGET_DIR)/..."
	$(CD) $(TARGET_DIR) && $(SYS_PYTHON) -m http.server

requirements: $(VENV)
	@$(ECHO) "Installing requirements..."
	$(PIP) install -r $(PIP_REQUIRE)
