TARGET := exercise
OBJS := main.o
LIB_USER := 
LIB_USER_OBJS :=  
OPTIONS := -g -fopenmp 
INC_FLAGS := 
LINK_FLAGS := -fopenmp
CFLAGS := $(OPTIONS) $(INC_FLAGS)
CXXFLAGS := $(OPTIONS) $(INC_FLAGS)
CC := gcc
CXX := g++
all	: $(TARGET) $(LIB_USER)
$(TARGET): $(OBJS) $(LIB_USER)
	@$(CXX) -o $@ $(OBJS) $(LIB_USER) $(LINK_FLAGS)
	@echo -e "\033[0;33m Generated $@\033[0m"
$(LIB_USER):	$(LIB_USER_OBJS)
	@ar -rcs $@ $^
	@echo -e "\033[0;32m LINK	$@	by	$^\033[0m"
%.o	:	%.c
	@$(CC) -c -fPIC $(CFLAGS) $< -o $@
	@echo -e "\033[0;32m CC	$@\033[0m"
%.o	:	%.cpp
	$(CXX) -c -fPIC $(CXXFLAGS) $< -o $@
	@echo -e "\033[0;32m CXX	$@\033[0m"
clean:
	@rm $(TARGET) $(LIB_USER) *.o
	@echo -e "\033[0;34m Removed all TARGET and objects\033[0m"

