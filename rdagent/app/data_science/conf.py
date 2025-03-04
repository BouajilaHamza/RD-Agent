from rdagent.app.kaggle.conf import KaggleBasePropSetting
from rdagent.core.conf import ExtendedSettingsConfigDict


class DataScienceBasePropSetting(KaggleBasePropSetting):
    model_config = ExtendedSettingsConfigDict(env_prefix="DS_", protected_namespaces=())

    # Main components
    ## Scen
    scen: str = "rdagent.scenarios.data_science.scen.KaggleScen"
    """Scenario class for data mining model"""

    ## Workflow Related
    consecutive_errors: int = 5

    debug_timeout: int = 600
    """The timeout limit for running on debugging data"""
    full_timeout: int = 3600
    """The timeout limit for running on full data"""

    # BO related
    bo_mode: bool = True

    idea_bo_step: int = 3
    """The step size for idea generation BO"""

    component_bo_step: int = 3
    """The step size for component selection BO"""



DS_RD_SETTING = DataScienceBasePropSetting()
