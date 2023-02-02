from unittest import mock
import pytest
from uuid import uuid4

from pdc_logger.logger import create_logger
from pdc_logger.exit_report import ExitReport

def test_basic_logger():
    
    logger = create_logger(__name__, sync_cloud=True)
    
    logger.warning(f"ini warnin2g {uuid4()}")
    logger.info(f"ini info {uuid4()}")
    logger.info(f"ini info {uuid4()}")
    logger.info(f"ini info {uuid4()}")
    logger.info(f"ini info {uuid4()}")
    logger.info(f"ini info {uuid4()}")
    logger.error("test error")
    
    
def test_basic_exit_report():
    
    try:
    
        with ExitReport() as er:
            
            raise Exception("blue2s")
    
    except:
        pass
    
    
def test_not_reporting():
    
    with mock.patch('pdc_logger.exit_report.logger.error') as logger:
        
        with ExitReport() as er:
            
            print("test")
            
        logger.assert_not_called()
        
    
    with pytest.raises(Exception):
        
        with mock.patch('pdc_logger.exit_report.logger.error') as logger:
        
            with ExitReport() as er:
                
                raise Exception('asdasdads')
                
            logger.assert_called()
        
        
        