import folium
import pandas as pd
import time

def gen_map_binary_categories(lat_series, lng_series, flag_series, 
                              output_path=f'./{time.localtime()}.html',
                              center=[22.6, 114.083333], zoom_start=11):
    
    """plot points of binary categories on the base map with folium
    
    Args:
        lat_series (pandas.Series): the series of latitude
        lng_series (pandas.Series): the series of longitude
        flag_series (pandas.Series): the series of flags
    
    """
    
    map = folium.map.FeatureGroup()
    for lat, lng, flag in zip(lat_series, lng_series, flag_series):
        
        if flag == 1:
            map.add_child(
                folium.Circle(
                    [lat, lng],
                    radius=5,
                    color='crimson',
                    fill=True,
                    fill_color='crimson',
                    fill_opacity=0.5
                )
            )
            
        elif flag == 0:
            map.add_child(
                folium.Circle(
                    [lat, lng],
                    radius=5,
                    color='#3186cc',
                    fill=True,
                    fill_color='#3186cc',
                    fill_opacity=0.5
                )
            )
            
    base_map = folium.Map(location=center, zoom_start=zoom_start)
    base_map.add_child(map)
    base_map.save(output_path)


def public_service_plot(output_path):
    
    """(DEPRECATED) plot points of multiple categories on the base map with folium
    
    # TODO: may need to redesign to avoid hard-coding and increase flexibility to 
            un-defined number of categories.
    
    """
    
    ps_data = pd.read_csv(output_path)
    ps = folium.map.FeatureGroup()
    for lat, lng, type_ in zip(ps_data.lat, ps_data.lng, ps_data.type):
        if type_ == 1:
            ps.add_child(
                folium.Circle(
                    [lat, lng],
                    radius=8,
                    color='#5882FA',
                    fill=True,
                    fill_color='#5882FA',
                    fill_opacity=0.5
                )
            )
        #elif type_ == 2:
            #ps.add_child(
                #folium.Circle(
                    #[lat, lng],
                    #radius=8,
                    #color='#298A08',
                    #fill=True,
                    #fill_color='#298A08',
                    #fill_opacity=0.5
                #)
            #)
        elif type_ == 3:
            ps.add_child(
                folium.Circle(
                    [lat, lng],
                    radius=8,
                    color='#8A0886',
                    fill=True,
                    fill_color='#8A0886',
                    fill_opacity=0.5
                )
            )
        elif type_ == 4:
            ps.add_child(
                folium.Circle(
                    [lat, lng],
                    radius=8,
                    color='crimson',
                    fill=True,
                    fill_color='crimson',
                    fill_opacity=0.5
                )
            )
        elif type_ == 5:
            ps.add_child(
                folium.Circle(
                    [lat, lng],
                    radius=8,
                    color='#FE9A2E',
                    fill=True,
                    fill_color='#FE9A2E',
                    fill_opacity=0.5
                )
            )
    sz_map = folium.Map(location=[22.6, 114.083333], zoom_start=11)
    sz_map.add_child(ps)
    sz_map.save(output_path)

if __name__ == '__main__':
    public_service_plot()