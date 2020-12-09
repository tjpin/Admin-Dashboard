from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd_extensions.akivymd.uix.piechart import AKPieChart
from kivymd.uix.datatables import MDDataTable
from hover import HoverIconList
from kivy.metrics import dp


class Dashboard(MDBoxLayout):
    def __init__(self, **kwargs):
        super(Dashboard, self).__init__(**kwargs)

        self.update_tables()
        self.draw_chart()

    def update_tables(self):
        dt = MDDataTable(size_hint=(1, 1),
                         elevation=-1,
                         column_data=[
                             ("Product", dp(30)),
                             ("Order ID", dp(30)),
                             ("Purchased On", dp(30)),
                             ("Amount", dp(30)),
                             ("Tracking", dp(30)),
                             ("Status", dp(30)),
                         ],
                         row_data=[
                             (
                                 "MacBook Pro",
                                 "#325689526",
                                 "8th Dec 2020",
                                 "& 1255.99",
                                 "GDKJSBC45",
                                 ("alert", [255 / 256, 165 / 256, 0, 1], "Pending")
                             ),
                             (
                                 "iPhone 11 Pro",
                                 "#325689526",
                                 "8th Dec 2020",
                                 "& 105.99",
                                 "GDKJSBC45",
                                 ("checkbox-marked-circle", [0, 1, 0, 1], "Delivered")
                             ),
                             (
                                 "MacBook Air",
                                 "#325689526",
                                 "8th Dec 2020",
                                 "& 120.00",
                                 "GDKJSBC45",
                                 ("checkbox-marked-circle", [0, 1, 0, 1], "Delivered")
                             ),
                             (
                                 "Oppo A20",
                                 "#325689526",
                                 "8th Dec 2020",
                                 "& 75.00",
                                 "GDKJSBC45",
                                 ("checkbox-marked-circle", [0, 1, 0, 1], "Delivered")
                             ),
                             (
                                 "Samsung A50",
                                 "#325689526",
                                 "8th Dec 2020",
                                 "& 88.00",
                                 "GDKJSBC45",
                                 ("alert-circle", [1, 0, 0, 1], "Canceled")
                             ),
                             (
                                 "MacBook Pro",
                                 "#327689146",
                                 "8th Dec 2020",
                                 "& 1205.99",
                                 "GDKJSBC45",
                                 ("checkbox-marked-circle", [0, 1, 0, 1], "Delivered")
                             )
                         ])
        self.ids.display.add_widget(dt)

    def draw_chart(self):
        self.items = [{
            "Electronics": 40,
            "Laptops": 20,
            "Shoes": 20,
            "iPhones": 20
        }]
        self.piechart = AKPieChart(
            items=self.items, pos_hint={'center_x': 0.5, 'center_y': .4},
            size_hint=[None, None],
            size=(dp(200), dp(200))
        )
        self.ids.pchart.add_widget(self.piechart)


class MainApp(MDApp):
    def build(self):
        return Dashboard()


if __name__ == "__main__":
    MainApp().run()
