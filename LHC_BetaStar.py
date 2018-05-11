import numpy as np
import TimberManager as tm

class BetaStar:
        def __init__(self, timber_variable, IP=0):
                
                timber_variable_BETA = None
                if type(timber_variable) is str:
                        print 'type var'
                        if not (IP ==1 or IP==5):
                                raise ValueError('You need to specify with IP! (1 or 5)')
                        dict_timber = tm.parse_timber_file(timber_variable, verbose=True)
                        if IP == 1:
                                timber_variable_BETA = dict_timber[get_variable_dict['BETASTAR_IP1']]
                        elif IP == 5:
                                timber_variable_BETA = dict_timber[get_variable_dict['BETASTAR_IP5']]
                                
                elif hasattr(timber_variable, '__getitem__'):
                        
                        try:
                                if IP == 1:
                                        timber_variable_BETA = timber_variable['HX:BETASTAR_IP1']
                                elif IP == 5: 
                                        timber_variable_BETA = timber_variable['HX:BETASTAR_IP5']
                        except:
                                print '# BetaStar : No BetaStar Information! Returning -1'
                                return -1
                        
                self.t_stamps = timber_variable_BETA.t_stamps
                self.beta = timber_variable_BETA.values


                self.beta     = np.array(np.float_(self.beta)).ravel()
                self.t_stamps = np.array(np.float_(self.t_stamps))

        def nearest_older_sample(self, t_obs, flag_return_time=False):
                ind_min = np.argmin(np.abs(self.t_stamps - t_obs))
                if self.t_stamps[ind_min] > t_obs:
                        ind_min -= 1
                if flag_return_time:    
                        if ind_min == -1:
                                return 0.*self.beta[ind_min], -1
                        else:   
                                return self.beta[ind_min], self.t_stamps[ind_min]
                else:
                        if ind_min == -1:
                                return 0.*self.beta[ind_min]
                        else:   
                                return self.beta[ind_min]
                                


def get_variable_dict():
        var_dict = {}
        var_dict['BETASTAR_IP1'] = 'HX:BETASTAR_IP1'
        var_dict['BETASTAR_IP5'] = 'HX:BETASTAR_IP5'
        #var_dict['LUMI_LEVEL_ENABLE_IP5'] = 'LUMILEVELING.IP5:ENABLE'

        return var_dict

def variable_list():
        var_list = []
        var_list += get_variable_dict().values()

        return var_list
