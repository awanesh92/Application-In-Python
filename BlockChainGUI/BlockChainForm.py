from tkinter import *
from tkinter import ttk
from blockchain import blockexplorer

class BlockForm:
    def __init__(self,master):
        master.title('BlockChain Query Form')
        master.resizable(False, False)
        master.configure(background = '#e1d8b9')

        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#e1d8b9')
        self.style.configure('TButton', background = '#e1d8b9')
        self.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))      

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        self.logo = PhotoImage(file = 'Blocklogo.png')
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, text = 'Welcome to BlockChain Explorer!', style = 'Header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 300,
                  text = ("We Will get the latest block on the blockchain \
                          after which you can query on the other details listed in API")).grid(row = 1, column = 1)
        
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()


        ttk.Label(self.frame_content, text = 'Hash No. to run query on the API').grid(row = 3, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Details:').grid(row = 3, column = 2, padx = 5, sticky = 'sw')


        self.hash_no = ttk.Entry(self.frame_content, width = 30, font = ('Arial', 10))
        self.details = StringVar()
        self.combobox = ttk.Combobox(self.frame_content, textvariable = self.details)
        self.combobox.config(values = ('hash','version','previous_block','merkle_root','time'
                                  'bits','fee','nonce','n_tx','size','block_index','main_chain','height','received_time','relayed_by','transactions'))
                
        self.hash_no.grid(row = 4, column = 0, padx = 5,sticky = 'sw')
        self.combobox.grid(row = 4, column = 2, columnspan = 2, padx = 5, sticky = 'sw')

        self.display_hashvalue =ttk.Label(self.frame_content, text = '', style = 'Header.TLabel')
        self.display_hashvalue.grid(row = 2, column = 0,columnspan =3)


        self.display_value =ttk.Label(self.frame_content, text = '', style = 'Header.TLabel')
        self.display_value.configure(font = ('Times New Roman', 12, 'bold'),foreground='blue')
        self.display_value.grid(row = 7, column = 0,columnspan =3)

        
        ttk.Label(self.frame_content, text = 'Query to Fetch Latest Block on BlockChain').grid(row = 5, column = 0, padx = 5, sticky = 'w')
        ttk.Label(self.frame_content, text = 'Query to Details attribute from the Latest Block on BlockChain').grid(row = 5, column = 2, padx = 5, sticky = 'w')
        ttk.Button(self.frame_content, text = 'QueryLatestHashValue',
                   command = self.submit).grid(row = 6, column=0, padx = 5, pady = 5, sticky=W+E)
        ttk.Button(self.frame_content, text = 'QueryFetchDetails',
                   command = self.submitquery).grid(row = 6, column=2 , padx = 5, pady = 5, sticky=W+E)


    def submit(self):
        self.h = blockexplorer.get_latest_block()
        self.display_hashvalue.configure(font = ('Arial', 12, 'bold'))
        self.display_hashvalue['text']=self.h.hash

    def submitquery(self):
        action=self.details.get()
        if len(self.hash_no.get())==0:
            b=blockexplorer.get_block(self.display_hashvalue['text'])
        else:
            b=blockexplorer.get_block(self.hash_no.get())

        if action == 'hash':
            self.display_value['text'] = b.hash
        elif action == 'version':
            self.display_value['text'] = b.version
        elif action == 'previous_block':
            self.display_value['text'] = b.previous_block
        elif action == 'merkle_root':
            self.display_value['text'] = b.merkle_root
        elif action == 'time':
            self.display_value['text'] = b.time
        elif action == 'bits':
            self.display_value['text'] = b.bits
        elif action == 'fee':
            self.display_value['text'] = b.fee
        elif action == 'nonce':
            self.display_value['text'] = b.nonce
        elif action == 'n_tx':
            self.display_value['text'] = b.n_tx
        elif action == 'size':
            self.display_value['text'] = b.size
        elif action == 'block_index':
            self.display_value['text'] = b.block_index
        elif action == 'main_chain':
            self.display_value['text'] = b.main_chain
        elif action == 'height':
            self.display_value['text'] = b.height
        elif action == 'received_time':
            self.display_value['text'] = b.received_time
        elif action == 'relayed_by':
            self.display_value['text'] = b.relayed_by
        elif action == 'transactions':
            self.display_value['text'] = 'Since this type contains many txns and its attributes displaying only count of txns :'+str(len(b.transactions))

    
def main():
    root = Tk()
    bform = BlockForm(root)
    root.mainloop()

if __name__=='__main__':
    main()
