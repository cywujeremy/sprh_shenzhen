import folium
import pandas as pd


def sprh_plot():
    sprh_data = pd.read_csv("D:/OneDriveLocal/OneDrive/学习/毕业/毕业论文/2020.02深圳/楼盘汇总.csv")
    sprh = folium.map.FeatureGroup()
    for lat, lng, sprh_mark in zip(sprh_data.LAT, sprh_data.LNG, sprh_data.SPRH):
        if sprh_mark == 1:
            sprh.add_child(
                folium.Circle(
                    [lat, lng],
                    radius=5,
                    color='crimson',
                    fill=True,
                    fill_color='crimson',
                    fill_opacity=0.5
                )
            )
        elif sprh_mark == 0:
            sprh.add_child(
                folium.Circle(
                    [lat, lng],
                    radius=5,
                    color='#3186cc',
                    fill=True,
                    fill_color='#3186cc',
                    fill_opacity=0.5
                )
            )
    sz_map = folium.Map(location=[22.6, 114.083333], zoom_start=11)
    sz_map.add_child(sprh)
    sz_map.save('D:/OneDriveLocal/OneDrive/学习/毕业/毕业论文/2020.02深圳/分布图/01.html')


def public_service_plot():
    ps_data = pd.read_csv("D:/OneDriveLocal/OneDrive/学习/毕业/毕业论文/2020.02深圳/xls/公共服务POI汇总.csv")
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
    sz_map.save('D:/OneDriveLocal/OneDrive/学习/毕业/毕业论文/2020.02深圳/分布图/public_services_0413.html')

if __name__ == '__main__':
    public_service_plot()