from pdc_logger.logger import create_logger
from pdc_logger.exit_report import ExitReport

def test_basic_logger():
    
    logger = create_logger(__name__, sync_cloud=True)
    
    logger.warning("ini warnin2g")
    
    
def test_basic_exit_report():
    
    try:
    
        with ExitReport() as er:
            
            raise Exception("blue2s")
    
    except:
        pass