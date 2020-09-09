import pandas as pd
import matplotlib.pyplot as plt

sample_data = pd.read_csv('data.csv')


def graph_time_as(gas=None):
    
    if gas is None:
        print("Need to provide a gas type!")
    
    elif gas == 'CO2':
        plt.plot(sample_data.TIME, sample_data.CO2)
        
    elif gas == 'CO':
        plt.plot(sample_data.TIME, sample_data.CO)
    
    elif gas == 'PM10':
        plt.plot(sample_data.TIME, sample_data.PM10)    
    
    elif gas== 'PM25':
        plt.plot(sample_data.TIME, sample_data.PM25)
    
    elif gas== 'PM100':
        plt.plot(sample_data.TIME, sample_data.PM100)
    
    elif gas== 'NO2':
        plt.plot(sample_data.TIME, sample_data.NO2)
   
    
    plt.xlabel('Time')
    plt.ylabel(str(gas))
    plt.title('Graph Time-{}'.format(gas))
    plt.legend(str(gas))
    plt.show()

    
graph_time_as('CO2')
graph_time_as('CO')
graph_time_as('Pm10')
graph_time_as('PM25')
graph_time_as('PM100')
graph_time_as('NO2')
