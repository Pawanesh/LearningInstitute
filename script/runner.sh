# Setting base directories
export LI_RUNTIME=/Users/pawgupta0/Pawanesh/runenv
export LI_HOME=/Users/pawgupta0/Pawanesh/development/LearningInstitute

# Setting generic envs
export LI_ENV=dev
export LI_APP=$LI_HOME/app
export LI_LIB=$LI_HOME/lib
export LI_SCRIPT=$LI_HOME/script
export LI_CONFIG=$LI_HOME/config

export LI_LOG=$LI_RUNTIME/log

export LD_LIBRARY_PATH=$LI_LIB:$LD_LIBRARY_PATH
export PYTHONPATH=$LI_LIB:$PYTHONPATH

# Running command
python $*