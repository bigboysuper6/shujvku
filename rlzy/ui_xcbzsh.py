def xcbzsh_ui():
    self.cxjg_jlxx_wd = tk.Tk()
    self.cxjg_jlxx_wd.title('信息摘要')
    self.cxjg_jlxx_wd.geometry('1000x600')
    self.biaotou = tk.Label(self.cxjg_jlxx_wd,
                            text='------------档案编号---------------姓名---------性别--------职位分类---------电话--------------档案状态---------',
                            bg='white', fg='black', font=('Arial', 15), width=90, height=1)
    self.biaotou.place(x=2, y=2)
    self.jlxx_text = Text(self.cxjg_jlxx_wd, width=124, height=33)
    self.jlxx_text.place(x=0, y=30)
    self.biaotou2 = tk.Label(self.cxjg_jlxx_wd, text='本表仅显示查询前十条信息', bg='white', fg='black', font=('Arial', 15),
                             width=90, height=1)
    self.biaotou2.place(x=1, y=500)
    self.jlxx_ind = -1

    if len(self.cxjg) >= 1:
        self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(18, self.cxjg[0][1]) + '        ' + self.bkg(5,
                                                                                                             self.cxjg[
                                                                                                                 0][
                                                                                                                 8]) + '        ' + self.bkg(
            2, self.cxjg[0][9]) + '        ' + self.bkg(6, self.cxjg[0][5]) + '        ' + self.bkg(12,
                                                                                                    self.cxjg[0][
                                                                                                        11]) + '        ' + self.bkg(
            3, self.cxjg[0][-1]) + '\n\n')
        self.jlxx_text.tag_add('link1', '1.5', '1.7')
        self.jlxx_text.tag_config('link1', foreground='green', underline=True)
        self.jlxx_text.tag_bind('link1', '<Button-1>', self.click1)
    if len(self.cxjg) >= 2:
        self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(18, self.cxjg[1][1]) + '        ' + self.bkg(5,
                                                                                                             self.cxjg[
                                                                                                                 1][
                                                                                                                 8]) + '        ' + self.bkg(
            2, self.cxjg[1][9]) + '        ' + self.bkg(6, self.cxjg[1][5]) + '        ' + self.bkg(12,
                                                                                                    self.cxjg[1][
                                                                                                        11]) + '        ' + self.bkg(
            3, self.cxjg[1][-1]) + '\n\n')
        self.jlxx_text.tag_add('link2', '3.5', '3.7')
        self.jlxx_text.tag_config('link2', foreground='green', underline=True)
        self.jlxx_text.tag_bind('link2', '<Button-1>', self.click2)
    if len(self.cxjg) >= 3:
        self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(18, self.cxjg[2][1]) + '        ' + self.bkg(5,
                                                                                                             self.cxjg[
                                                                                                                 2][
                                                                                                                 8]) + '        ' + self.bkg(
            2, self.cxjg[2][9]) + '        ' + self.bkg(6, self.cxjg[2][5]) + '        ' + self.bkg(12,
                                                                                                    self.cxjg[2][
                                                                                                        11]) + '        ' + self.bkg(
            3, self.cxjg[2][-1]) + '\n\n')
        self.jlxx_text.tag_add('link3', '5.5', '5.7')
        self.jlxx_text.tag_config('link3', foreground='green', underline=True)
        self.jlxx_text.tag_bind('link3', '<Button-1>', self.click3)
    if len(self.cxjg) >= 4:
        self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(18, self.cxjg[3][1]) + '        ' + self.bkg(5,
                                                                                                             self.cxjg[
                                                                                                                 3][
                                                                                                                 8]) + '        ' + self.bkg(
            2, self.cxjg[3][9]) + '        ' + self.bkg(6, self.cxjg[3][5]) + '        ' + self.bkg(12,
                                                                                                    self.cxjg[3][
                                                                                                        11]) + '        ' + self.bkg(
            3, self.cxjg[3][-1]) + '\n\n')
        self.jlxx_text.tag_add('link4', '7.5', '7.7')
        self.jlxx_text.tag_config('link4', foreground='green', underline=True)
        self.jlxx_text.tag_bind('link4', '<Button-1>', self.click4)
    if len(self.cxjg) >= 5:
        self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(18, self.cxjg[4][1]) + '        ' + self.bkg(5,
                                                                                                             self.cxjg[
                                                                                                                 4][
                                                                                                                 8]) + '        ' + self.bkg(
            2, self.cxjg[4][9]) + '        ' + self.bkg(6, self.cxjg[4][5]) + '        ' + self.bkg(12,
                                                                                                    self.cxjg[4][
                                                                                                        11]) + '        ' + self.bkg(
            3, self.cxjg[4][-1]) + '\n\n')
        self.jlxx_text.tag_add('link5', '9.5', '9.7')
        self.jlxx_text.tag_config('link5', foreground='green', underline=True)
        self.jlxx_text.tag_bind('link5', '<Button-1>', self.click5)
    if len(self.cxjg) >= 6:
        self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(18, self.cxjg[5][1]) + '        ' + self.bkg(5,
                                                                                                             self.cxjg[
                                                                                                                 5][
                                                                                                                 8]) + '        ' + self.bkg(
            2, self.cxjg[5][9]) + '        ' + self.bkg(6, self.cxjg[5][5]) + '        ' + self.bkg(12,
                                                                                                    self.cxjg[5][
                                                                                                        11]) + '        ' + self.bkg(
            3, self.cxjg[5][-1]) + '\n\n')
        self.jlxx_text.tag_add('link6', '11.5', '11.7')
        self.jlxx_text.tag_config('link6', foreground='green', underline=True)
        self.jlxx_text.tag_bind('link6', '<Button-1>', self.click6)
    if len(self.cxjg) >= 7:
        self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(18, self.cxjg[6][1]) + '        ' + self.bkg(5,
                                                                                                             self.cxjg[
                                                                                                                 6][
                                                                                                                 8]) + '        ' + self.bkg(
            2, self.cxjg[6][9]) + '        ' + self.bkg(6, self.cxjg[6][5]) + '        ' + self.bkg(12,
                                                                                                    self.cxjg[6][
                                                                                                        11]) + '        ' + self.bkg(
            3, self.cxjg[6][-1]) + '\n\n')
        self.jlxx_text.tag_add('link7', '13.5', '13.7')
        self.jlxx_text.tag_config('link7', foreground='green', underline=True)
        self.jlxx_text.tag_bind('link7', '<Button-1>', self.click7)
    if len(self.cxjg) >= 8:
        self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(18, self.cxjg[7][1]) + '        ' + self.bkg(5,
                                                                                                             self.cxjg[
                                                                                                                 7][
                                                                                                                 8]) + '        ' + self.bkg(
            2, self.cxjg[7][9]) + '        ' + self.bkg(6, self.cxjg[7][5]) + '        ' + self.bkg(12,
                                                                                                    self.cxjg[7][
                                                                                                        11]) + '        ' + self.bkg(
            3, self.cxjg[7][-1]) + '\n\n')
        self.jlxx_text.tag_add('link8', '15.5', '15.7')
        self.jlxx_text.tag_config('link8', foreground='green', underline=True)
        self.jlxx_text.tag_bind('link8', '<Button-1>', self.click8)
    if len(self.cxjg) >= 9:
        self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(18, self.cxjg[8][1]) + '        ' + self.bkg(5,
                                                                                                             self.cxjg[
                                                                                                                 8][
                                                                                                                 8]) + '        ' + self.bkg(
            2, self.cxjg[8][9]) + '        ' + self.bkg(6, self.cxjg[8][5]) + '        ' + self.bkg(12,
                                                                                                    self.cxjg[8][
                                                                                                        11]) + '        ' + self.bkg(
            3, self.cxjg[8][-1]) + '\n\n')
        self.jlxx_text.tag_add('link9', '17.5', '17.7')
        self.jlxx_text.tag_config('link9', foreground='green', underline=True)
        self.jlxx_text.tag_bind('link9', '<Button-1>', self.click9)
    if len(self.cxjg) >= 10:
        self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(18, self.cxjg[9][1]) + '        ' + self.bkg(5,
                                                                                                             self.cxjg[
                                                                                                                 9][
                                                                                                                 8]) + '        ' + self.bkg(
            2, self.cxjg[9][9]) + '        ' + self.bkg(6, self.cxjg[9][5]) + '        ' + self.bkg(12,
                                                                                                    self.cxjg[9][
                                                                                                        11]) + '        ' + self.bkg(
            3, self.cxjg[9][-1]) + '\n\n')
        self.jlxx_text.tag_add('link10', '19.5', '19.7')
        self.jlxx_text.tag_config('link10', foreground='green', underline=True)
        self.jlxx_text.tag_bind('link10', '<Button-1>', self.click10)
    self.jlxx_text.config(state=DISABLED)