include Makefiles/CoreSources.inc.mk

TOP_MODULE = Main_Zynq_Wrapper

SOURCE_ROOT = ./

DEPS_RTL = \
	$(TYPES:%=$(SOURCE_ROOT)%) \
	$(MODULES:%=$(SOURCE_ROOT)%) \
	$(DEBUG_HELPERS:%=$(SOURCE_ROOT)%)

RSD_VERILATOR_DEFINITION = \
	+define+RSD_FUNCTIONAL_SIMULATION \
	+define+RSD_FUNCTIONAL_SIMULATION_VERILATOR \
	$(RSD_SRC_CFG) \

VERILATOR_DISABLED_WARNING = \
     -Wno-WIDTH \
     -Wno-INITIALDLY \
     -Wno-UNOPTFLAT \

VERILATOR_OPTION = \
	--xml-only \
	--flatten \
	--xml-output rsd.xml \
	-sv \
	--top-module $(TOP_MODULE) \
	$(VERILATOR_DISABLED_WARNING) \
	$(RSD_VERILATOR_DEFINITION) \
	+incdir+.

VERILATOR_TARGET_CXXFLAGS= \
	-D RSD_FUNCTIONAL_SIMULATION_VERILATOR \
	-D RSD_FUNCTIONAL_SIMULATION \
	-D RSD_VERILATOR_TRACE \
	-D RSD_MARCH_UNIFIED_MULDIV_MEM_PIPE \
	-Wno-attributes \

rsd.xml:
	$(VERILATOR_BIN) $(VERILATOR_OPTION) $(DEPS_RTL)

all: rsd.xml
