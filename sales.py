from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.list import OneLineListItem,ThreeLineAvatarListItem,ThreeLineAvatarIconListItem,ImageLeftWidget,IconRightWidget
from kivymd.uix.list import MDList
##from kivy.uix.scrollview import Scrollview
from kivymd.uix.scrollview import MDScrollView
import sqlite3
from kivymd.uix.textfield import MDTextField
##from main import SalesScreen
##from kivymd.uix.scrollview import MDScrollview

##Builder.load_file('sale.kv')



def read_img(filename,data):
    with open(filename, 'wb') as file:
        file.write(data)
    return filename

class SalesBoard(MDScrollView):
    conn=None
    curs=None

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
##    def commence(self):
        self.conn=sqlite3.connect('Sale_DBASE.db')
        self.curs=self.conn.cursor()
        self.app=MDApp.get_running_app()
        

        

        
       
        
        
        self.read_all()
    def read_all(self):
       
                                   

##        my_app=MDApp.get_running_app()
##        print('MY APP=',my_app)
##        sales_screen=my_app.root.ids.sales2
        

        
        self.curs.execute("""SELECT * FROM Properties""")
        self.results=self.curs.fetchall()
        list_view=MDList()
##        scroll=MDScrollView()
        for i in self.results:
            location=str(i[0])
            erf=str(i[1])
            value=str(i[2])
            pic=i[3]
            filename='{}{}.jpeg'.format(erf,location)
            my_pic=read_img(filename,pic)

            img_wid=ImageLeftWidget(source=my_pic)
            
           
            pri_txt='Location:{}'.format(location)
            sec_text='Lot Number:{}'.format(erf)
            tert_text='Value:BWP{}'.format(value)
            idx='{}-{}'.format(erf,location)

            ic=IconRightWidget(icon="minus",on_press=self.sold_property,id=idx)
            
            items=ThreeLineAvatarIconListItem(text=pri_txt,secondary_text=sec_text,tertiary_text=tert_text)
            items.add_widget(img_wid)
            items.add_widget(ic)
            list_view.add_widget(items)
        self.add_widget(list_view)
##        self.add_widget(scroll)

    def sold_property(self,item):
        erff,loc=item.id.split('-')
        erf=int(erff)
        self.curs.execute("""DELETE FROM Properties wHERE LOTNUMBER=:num AND LOCATION=:loc""",{'num':erf,'loc':loc})
        self.reset()

##        print(erf,loc)
##        DBase.delete_item(lot_num,location)
##        self.reset()

    def refresh(self):
        self.clear_widgets()
        
    def search_result(self,value):
        val=value.title()
        self.curs.execute("""SELECT * FROM Properties WHERE INSTR(LOCATION,:val)""",{'val':val})
        return self.curs.fetchall()
        
    def self_show(self):

        
        
##        sales_screen=my_app.root.ids.sales2
##        result=sales_screen.manager.get_screen("sales").ids.searcher.text
##        
##        result=searcher.text
        result='Gaborone'
        items=self.search_result(result)
##        my_app.root.ids.searcher.text=''
        list_view=MDList()
        if items:
            self.refresh()
            for i in items:
                location=str(i[0])
                erf=str(i[1])
                value=str(i[2])
                pic=i[3]
                filename='{}{}.jpeg'.format(erf,location)
                my_pic=read_img(filename,pic)

                img_wid=ImageLeftWidget(source=my_pic)
            
           
                pri_txt='Location:{}'.format(location)
                sec_text='Lot Number:{}'.format(erf)
                tert_text='Value:BWP{}'.format(value)
                idx='{}-{}'.format(erf,location)

                ic=IconRightWidget(icon="minus",on_press=self.sold_property,id=idx)
            
                items=ThreeLineAvatarIconListItem(text=pri_txt,secondary_text=sec_text,tertiary_text=tert_text)
                items.add_widget(img_wid)
                items.add_widget(ic)
                list_view.add_widget(items)
            self.add_widget(list_view)
##            self.add_widget(scroll)
##            self.add_widget(list_view)

    def reset(self):
        self.refresh()

        self.curs.execute("""SELECT * FROM Properties""")
        results=self.curs.fetchall()

##        results=self.results
##        print('RESULTS=',results)
        list_view=MDList()
##        scroll=MDScrollView()
        for i in results:
            location=str(i[0])
            erf=str(i[1])
            value=str(i[2])
            pic=i[3]
            filename='{}{}.jpeg'.format(erf,location)
            my_pic=read_img(filename,pic)

            img_wid=ImageLeftWidget(source=my_pic)
            
           
            pri_txt='Location:{}'.format(location)
            sec_text='Lot Number:{}'.format(erf)
            tert_text='Value:BWP{}'.format(value)
            idx='{}-{}'.format(erf,location)

            ic=IconRightWidget(icon="minus",on_press=self.sold_property,id=idx)
            
            items=ThreeLineAvatarIconListItem(text=pri_txt,secondary_text=sec_text,tertiary_text=tert_text)
            items.add_widget(img_wid)
            items.add_widget(ic)
            list_view.add_widget(items)
##        scroll.add_widget(list_view)
##        self.add_widget(scroll)
        self.add_widget(list_view)





        
    

    
        
        
        
    
