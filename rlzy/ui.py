from tkinter import *
import datetime
import ui_acc_sql as uas
import tkinter as tk
from tkinter import ttk


class ui():

    def a(self):
        print('按键')

    def xcgl_ui(self):
        pass

    # 补空格函数
    def bkg(self, leng, value):
        kg = ' '
        result_str = value
        if len(result_str) < leng:
            result_str = result_str + kg * (leng - len(result_str))
        return result_str

    # 注册按钮权限更改
    def b1(self):
        self.aut = '人事专员'

    def b2(self):
        self.aut = '人事经理'

    def b3(self):
        self.aut = '薪酬专员'

    def b4(self):
        self.aut = '薪酬经理'

    # 按个人信息查询选择条件
    def a1(self):
        self.cxlb = 'bh'

    def a2(self):
        self.cxlb = 'xm'

    def a3(self):
        self.cxlb = 'zw'

    def a4(self):
        self.cxlb = 'xb'

    # 按个人信息查询确认查询，条件判断
    def grxx_querenchaxun(self):
        self.cxjg = None
        if self.cxlb == 'wx':
            self.text4['text'] = '请选择查询条件'
            return
        elif self.cxlb == 'bh':
            self.cxjg = uas.dacx_bh(self.agrxxcx_en.get())
        elif self.cxlb == 'xm':
            self.cxjg = uas.dacx_xm(self.agrxxcx_en.get())
        elif self.cxlb == 'zw':
            self.cxjg = uas.dacx_zw(self.agrxxcx_en.get())
        elif self.cxlb == 'xb':
            self.cxjg = uas.dacx_xb(self.agrxxcx_en.get())
        else:
            self.text4['text'] = '查询系统出错'
            return
        if len(self.cxjg) != 0:
            self.cxjg_jlxx_ui()
        else:
            self.text4['text'] = '未查询到符合条件的结果'
            return

    # 按机构查询确认查询
    def jgcx_querenchaxun(self):
        self.i_jgcx = self.i_cb.get()
        self.ii_jgcx = self.ii_cb.get()
        self.iii_jgcx = self.iii_cb.get()
        self.zwfl_jgcx = self.zwfl_cb.get()
        if len(self.i_jgcx) == 0 and len(self.ii_jgcx) == 0 and len(self.iii_jgcx) == 0 and len(self.zwfl_jgcx) == 0:
            self.text5['text'] = '请输入查询条件'
            return
        else:
            self.cxjg = uas.dacx_jgcx(self.i_jgcx, self.ii_jgcx, self.iii_jgcx, self.zwfl_jgcx)
            if len(self.cxjg) != 0:
                self.cxjg_jlxx_ui()
                return
            else:
                self.text5['text'] = '未查询到符合条件的结果'

    # 简略信息详情选择条
    def click1(self, s):
        self.jlxx_ind = 0
        print(self.cxjg[self.jlxx_ind][:])
        self.dafh_ui(self.cxjg[self.jlxx_ind][:])

    def click2(self, s):
        self.jlxx_ind = 1
        self.dafh_ui(self.cxjg[self.jlxx_ind][:])

    def click3(self, s):
        self.jlxx_ind = 2
        self.dafh_ui(self.cxjg[self.jlxx_ind][:])

    def click4(self, s):
        self.jlxx_ind = 3
        self.dafh_ui(self.cxjg[self.jlxx_ind][:])

    def click5(self, s):
        self.jlxx_ind = 4
        self.dafh_ui(self.cxjg[self.jlxx_ind][:])

    def click6(self, s):
        self.jlxx_ind = 5
        self.dafh_ui(self.cxjg[self.jlxx_ind][:])

    def click7(self, s):
        self.jlxx_ind = 6
        self.dafh_ui(self.cxjg[self.jlxx_ind][:])

    def click8(self, s):
        self.jlxx_ind = 7
        self.dafh_ui(self.cxjg[self.jlxx_ind][:])

    def click9(self, s):
        self.jlxx_ind = 8
        self.dafh_ui(self.cxjg[self.jlxx_ind][:])

    def click10(self, s):
        self.jlxx_ind = 9
        self.dafh_ui(self.cxjg[self.jlxx_ind][:])

    # 三级联动
    def ix_jg(self, *args):
        self.i_jg = self.i_cb.get()
        self.list = [' ']
        self.list2 = [' ']
        for i in uas.acc_sql_ii(self.i_jg):
            for j in i:
                self.list.append(j)
        self.ii_cb['values'] = self.list
        self.ii_cb.current(0)
        self.iii_cb['values'] = self.list2
        self.iii_cb.current(0)

        # 三级联动

    def iix_jg(self, *args):
        self.ii_jg = self.ii_cb.get()
        self.list = [' ']
        for i in uas.acc_sql_iii(self.ii_jg):
            for j in i:
                self.list.append(j)
        self.iii_cb['values'] = self.list
        self.iii_cb.current(0)

    # 返回登录界面函数
    def fanhuidenglu(self):
        try:
            self.sb_wd.destroy()
        except:
            pass
        try:
            self.zc_wd.destroy()
        except:
            pass
        self.loding_ui()

    # 返回管理界面函数
    def fanhuiguanli(self):
        try:
            self.dayw_wd.destroy()
        except:
            pass
        self.loding_success()

    # 返回档案业务选择界面
    def fanhuidangan(self):
        try:
            self.dacx_wd.destroy()
        except:
            pass
        self.danganyewu_ui()

    # 档案录入界面清除函数
    def qingchu(self):
        try:
            self.darr_wd.destroy()
        except:
            pass
        self.dalr_ui()

    # 档案详情界面回复修改
    def dashxg_hf(self):
        try:
            self.darr_wd.destroy()
        except:
            pass
        self.dafh_ui(self.fhjg)

    # 检查注册条件
    def check_zhuce(self):
        self.zhuce_result = uas.check_zhuche(self.zc_zh_en.get(), self.zc_mm_en.get(), self.aut)
        if self.zhuce_result:
            self.text2['text'] = '注册成功'
        else:
            self.text2['text'] = '注册失败：用户名为空或已存在或密码小于6位'

    # 检查登陆条件
    def check_loding(self):
        self.admin = []  # '-','人事经理'
        self.result = uas.check_password(self.zh_en.get(), self.mm_en.get())
        if self.result in ['人事专员', '人事经理', '薪酬专员', '薪酬经理']:
            self.admin = [self.zh_en.get(), self.result]
            self.loding_success()
        else:
            self.text1['text'] = '用户名或密码错误请重新输入'

    # 档案审核权限检查
    def dash(self):
        if self.admin[1] != '人事经理':
            self.text3['text'] = '您的权限不足, 请选择其他业务'
            return
        self.cxjg = uas.dacx_dsh()
        self.cxjg_jlxx_ui()

    # 薪酬标注审核权限检查
    def xcbz(self):
        if self.admin[1] != '薪酬经理':
            self.text3['text'] = '您的权限不足, 请选择其他业务'
            return
        self.cxjg = uas.xcbz_dsh()
        self.xcbzsh_ui()

    def ygxcsh(self):
        if self.admin[1] != '薪酬经理':
            self.text3['text'] = '您的权限不足, 请选择其他业务'
            return
        self.cxjg = uas.ygxc_sh()
        self.ygxcsh_ui()

    # 档案录入确认信息获取
    def queren(self):
        dangan_no = uas.cxda_no(self.i_cb.get(), self.ii_cb.get(), self.iii_cb.get())
        if dangan_no != False:
            dangan_no = self.today[:4] + dangan_no
            xingxi = [dangan_no,
                      self.i_cb.get(), self.ii_cb.get(), self.iii_cb.get(),
                      self.zwfl_cb.get(), self.zwmc_cb.get(), self.zc_cb.get(),
                      self.xm_en.get(), self.xb_cb.get(), self.em_en.get(),
                      self.dh_en.get(), self.qq_en.get(), self.sj_en.get(),
                      self.zz_en.get(), self.yb_en.get(),
                      self.gj_cb.get(), self.csd_en.get(), self.sr_en.get(), self.mz_cb.get(),
                      self.zjxy_cb.get(), self.zzmm_cb.get(), self.sfzh_en.get(), self.sbhm_en.get(),
                      int(self.nl_en.get()), self.xl_cb.get(), int(self.jynx_cb.get()), self.xlzy_cb.get(),
                      self.xcbz_cb.get(), self.khh_en.get(), self.zh_en.get(), self.admin[0], self.today,
                      self.tc_cb.get(), self.ah_cb.get(),
                      self.grll_tx.get(1.0, 1000.0),
                      self.jtgx_tx.get(1.0, 1000.0),
                      self.bz_tx.get(1.0, 1000.0), '待审核'
                      ]
            result_ins = uas.insert_dangan(xingxi)
            if result_ins:
                self.text7 = tk.Label(self.darr_wd, text='保存成功\n请退出！', bg='white', fg='black', font=('Arial', 15),
                                      width=15, height=5)
                self.text7.place(x=1200, y=0)
            else:
                self.text7 = tk.Label(self.darr_wd, text='保存失败！', bg='white', fg='black', font=('Arial', 15), width=30,
                                      height=1)
                self.text7.place(x=1050, y=265)
        else:
            self.text7 = tk.Label(self.darr_wd, text='保存失败！', bg='white', fg='black', font=('Arial', 15), width=29,
                                  height=1)
            self.text7.place(x=1050, y=265)

    # 薪酬标准确认信息录取
    def queren_xc(self):
        if self.ll.get() == '已复核':
            ll_ = 'yifuhe'
        elif self.ll.get() == '复核':
            ll_ = 'fuhe'

        xingxi = [self.aa.get(),
                  self.bb.get(), self.cc.get(),
                  self.today, self.ee.get(), self.ff.get(),
                  self.gg.get(), self.hh.get(), self.jj.get(),
                  self.kk.get(), ll_
                  ]
        result_ins = uas.insert_xcxm(xingxi)
        if result_ins:
            self.text7 = tk.Label(self.darr_wd, text='保存成功\n请退出！', bg='white', fg='black', font=('Arial', 15),
                                  width=15, height=5)
            self.text7.place(x=1200, y=0)
        else:
            self.text7 = tk.Label(self.darr_wd, text='保存失败！', bg='white', fg='black', font=('Arial', 15), width=30,
                                  height=1)
            self.text7.place(x=1050, y=265)

    # else:
    # self.text7 = tk.Label(self.darr_wd, text='保存失败！', bg='white', fg='black', font=('Arial', 15), width=29,
    #                       height=1)
    # self.text7.place(x=1050, y=265)

    def queren_ygxc(self):
        if self.ggg.get() == '待登记':
            ggg_ = 'daidengji'
        elif self.ggg.get() == '待复核':
            ggg_ = 'daifuhe'
        elif self.ggg.get() == '待发放':
            ggg_ = 'daifafang'

        xingxi = [self.aaa.get(),
                  self.bbb.get(), self.ccc.get(),
                  self.ddd.get(),
                  self.eee.get(), self.fff.get(), ggg_]
        result_ins = uas.insert_ygxcdj(xingxi)
        if result_ins:
            self.text7 = tk.Label(self.darr_wd, text='保存成功\n请退出！', bg='white', fg='black', font=('Arial', 15),
                                  width=15, height=5)
            self.text7.place(x=1200, y=0)
        else:
            self.text7 = tk.Label(self.darr_wd, text='保存失败！', bg='white', fg='black', font=('Arial', 15), width=30,
                                  height=1)
            self.text7.place(x=1050, y=265)

    # 复核通过确认信息获取
    def fuhetongguo(self):
        xingxi2 = [self.fhjg[1],
                   self.fhjg[2], self.fhjg[3], self.fhjg[4],
                   self.fhjg[5], self.fhjg[6], self.zc_cb.get(),
                   self.xm_en.get(), self.xb_cb.get(), self.em_en.get(),
                   self.dh_en.get(), self.qq_en.get(), self.sj_en.get(),
                   self.zz_en.get(), self.yb_en.get(),
                   self.gj_cb.get(), self.csd_en.get(), self.sr_en.get(), self.mz_cb.get(),
                   self.zjxy_cb.get(), self.zzmm_cb.get(), self.sfzh_en.get(), self.sbhm_en.get(),
                   int(self.nl_en.get()), self.xl_cb.get(), int(self.jynx_cb.get()), self.xlzy_cb.get(),
                   self.xcbz_cb.get(), self.khh_en.get(), self.zh_en.get(), self.fhjg[31], self.fhjg[32],
                   self.tc_cb.get(), self.ah_cb.get(),
                   self.grll_tx.get(1.0, 1000.0),
                   self.jtgx_tx.get(1.0, 1000.0),
                   self.bz_tx.get(1.0, 1000.0), '待审核'
                   ]
        uas.danganfuhe(xingxi2, self.admin[1], self.zt)

    # 档案状态更改
    def tgsh(self):
        self.zt = '归档'
        self.fuhetongguo()

    def scgd(self):
        self.zt = '已删除'
        self.fuhetongguo()

    def tjxg(self):
        self.zt = '待审核'
        self.fuhetongguo()

    ######################################################################################################################

    # 登录界面
    def loding_ui(self):
        try:
            self.dayw_wd.destroy()
        except:
            pass
        try:
            self.dacx_wd.destroy()
        except:
            pass
        self.wd = tk.Tk()
        self.wd.title('登陆')
        self.wd.geometry('1000x600')
        self.logo = tk.Label(self.wd, text='请登录', bg='white', fg='black', font=('Arial', 20), width=10, height=2)
        self.logo.place(x=430, y=30)
        self.zh_lb = tk.Label(self.wd, text='账号：', bg='white', fg='black', font=('Arial', 10), width=5, height=2)
        self.zh_lb.place(x=200, y=150)
        self.zh_en = tk.Entry(self.wd, show=None, font=('Arial', 14), width=50)
        self.zh_en.place(x=240, y=156)  # zh_en.get()获得输入内容
        self.mm_lb = tk.Label(self.wd, text='密码：', bg='white', fg='black', font=('Arial', 10), width=5, height=2)
        self.mm_lb.place(x=200, y=220)
        self.mm_en = tk.Entry(self.wd, show='*', font=('Arial', 14), width=50)
        self.mm_en.place(x=240, y=226)  # mm_en.get()获得输入内容
        self.zc_bt = tk.Button(self.wd, text='注册', font=('Arial', 12), width=10, height=1, command=self.zhuce_ui)
        self.zc_bt.place(x=230, y=450)
        self.dl_bt = tk.Button(self.wd, text='登录', font=('Arial', 12), width=10, height=1, command=self.check_loding)
        self.dl_bt.place(x=550, y=450)
        self.text1 = tk.Label(self.wd, text=' ')
        self.text1.place(x=0, y=540)
        self.wd.mainloop()

    # 注册界面
    def zhuce_ui(self):
        try:
            self.wd.destroy()
        except:
            pass
        self.aut = '人事专员'
        self.zc_wd = tk.Tk()
        self.zc_wd.title('注册')
        self.zc_wd.geometry('1000x600')
        self.logo = tk.Label(self.zc_wd, text='注册', bg='white', fg='black', font=('Arial', 20), width=10, height=2)
        self.logo.place(x=430, y=30)
        self.zc_zh_lb = tk.Label(self.zc_wd, text='输入账号：', bg='white', fg='black', font=('Arial', 10), width=10,
                                 height=2)
        self.zc_zh_lb.place(x=200, y=150)
        self.zc_zh_en = tk.Entry(self.zc_wd, show=None, font=('Arial', 14), width=50)
        self.zc_zh_en.place(x=280, y=156)  # zh_en.get()获得输入内容
        self.zc_mm_lb = tk.Label(self.zc_wd, text='输入密码：', bg='white', fg='black', font=('Arial', 10), width=10,
                                 height=2)
        self.zc_mm_lb.place(x=200, y=220)
        self.zc_mm_en = tk.Entry(self.zc_wd, show=None, font=('Arial', 14), width=50)
        self.zc_mm_en.place(x=280, y=226)  # mm_en.get()获得输入内容
        self.zc_zc_bt = tk.Button(self.zc_wd, text='确认注册', font=('Arial', 12), width=10, height=1,
                                  command=self.check_zhuce)
        self.zc_zc_bt.place(x=230, y=450)
        self.zc_dl_bt = tk.Button(self.zc_wd, text='返回登录', font=('Arial', 12), width=10, height=1,
                                  command=self.fanhuidenglu)
        self.zc_dl_bt.place(x=550, y=450)
        self.rb_var = tk.StringVar()
        self.zc_rb1 = tk.Radiobutton(self.zc_wd, text='人事专员', variable=self.rb_var, value='aaaa', command=self.b1)
        self.zc_rb1.place(x=300, y=300)
        self.zc_rb2 = tk.Radiobutton(self.zc_wd, text='人事经理', variable=self.rb_var, value='bbbb', command=self.b2)
        self.zc_rb2.place(x=500, y=300)
        self.zc_rb3 = tk.Radiobutton(self.zc_wd, text='薪酬专员', variable=self.rb_var, value='cccc', command=self.b3)
        self.zc_rb3.place(x=300, y=350)
        self.zc_rb4 = tk.Radiobutton(self.zc_wd, text='薪酬经理', variable=self.rb_var, value='ddddd', command=self.b4)
        self.zc_rb4.place(x=500, y=350)
        self.text2 = tk.Label(self.zc_wd, text=' ')
        self.text2.place(x=0, y=540)

    # 登陆成功选择业务界面
    def loding_success(self):
        try:
            self.wd.destroy()
        except:
            pass
        try:
            self.dacx_wd.destroy()
        except:
            pass
        self.sb_wd = tk.Tk()
        self.sb_wd.title('选择业务')
        self.sb_wd.geometry('1000x600')
        self.logo = tk.Label(self.sb_wd, text='>登陆成功<', bg='white', fg='black', font=('Arial', 20), width=10, height=2)
        self.logo.place(x=430, y=30)
        self.yw_lb = tk.Label(self.sb_wd, text='选择业务：', bg='white', fg='black', font=('Arial', 15), width=10, height=2)
        self.yw_lb.place(x=230, y=230)
        self.sb_da_bt = tk.Button(self.sb_wd, text='档案管理', font=('Arial', 12), width=20, height=2,
                                  command=self.danganyewu_ui)
        self.sb_da_bt.place(x=400, y=150)
        self.sb_xc_bt = tk.Button(self.sb_wd, text='薪酬管理', font=('Arial', 12), width=20, height=2,
                                  command=self.xcxz_ui)
        self.sb_xc_bt.place(x=400, y=300)
        self.sb_fh_bt = tk.Button(self.sb_wd, text='退出登录', font=('Arial', 8), width=10, height=1,
                                  command=self.fanhuidenglu)
        self.sb_fh_bt.place(x=0, y=0)
        self.huanying = tk.Label(self.sb_wd, text='欢迎您：', bg='white', fg='black', font=('Arial', 10), width=8, height=1)
        self.huanying.place(x=0, y=570)
        self.huanying1 = tk.Label(self.sb_wd, text=self.admin, bg='white', fg='black', font=('Arial', 10), width=20,
                                  height=1)
        self.huanying1.place(x=60, y=570)

    # 档案业务选择界面
    def danganyewu_ui(self):
        try:
            self.sb_wd.destroy()
        except:
            pass
        self.dayw_wd = tk.Tk()
        self.dayw_wd.title('选择档案业务')
        self.dayw_wd.geometry('1000x600')
        self.yw_lb = tk.Label(self.dayw_wd, text='选择档案业务：', bg='white', fg='black', font=('Arial', 15), width=12,
                              height=2)
        self.yw_lb.place(x=230, y=230)
        self.yw_cx_bt = tk.Button(self.dayw_wd, text='档案查询', font=('Arial', 12), width=20, height=2,
                                  command=self.dacx_ui)
        self.yw_cx_bt.place(x=400, y=150)
        self.yw_lr_bt = tk.Button(self.dayw_wd, text='档案录入', font=('Arial', 12), width=20, height=2,
                                  command=self.dalr_ui)
        self.yw_lr_bt.place(x=400, y=225)
        self.yw_sh_bt = tk.Button(self.dayw_wd, text='档案审核', font=('Arial', 12), width=20, height=2, command=self.dash)
        self.yw_sh_bt.place(x=400, y=300)
        self.sb_fh_bt1 = tk.Button(self.dayw_wd, text='退出登录', font=('Arial', 8), width=10, height=1,
                                   command=self.fanhuidenglu)
        self.sb_fh_bt1.place(x=0, y=0)
        self.yw_fh_bt2 = tk.Button(self.dayw_wd, text='<<返回管理', font=('Arial', 8), width=10, height=1,
                                   command=self.fanhuiguanli)
        self.yw_fh_bt2.place(x=87, y=0)
        self.huanying = tk.Label(self.dayw_wd, text='欢迎您：', bg='white', fg='black', font=('Arial', 10), width=8,
                                 height=1)
        self.huanying.place(x=0, y=570)
        self.huanying1 = tk.Label(self.dayw_wd, text=self.admin, bg='white', fg='black', font=('Arial', 10), width=20,
                                  height=1)
        self.huanying1.place(x=60, y=570)
        self.text3 = tk.Label(self.dayw_wd, text=' ')
        self.text3.place(x=0, y=540)

    # 档案查询选择条件界面
    def dacx_ui(self):
        try:
            self.dayw_wd.destroy()
        except:
            pass
        self.dacx_wd = tk.Tk()
        self.dacx_wd.title('档案查询')
        self.dacx_wd.geometry('1000x600')
        self.dacx_lb = tk.Label(self.dacx_wd, text='选择查询条件：', bg='white', fg='black', font=('Arial', 15), width=12,
                                height=2)
        self.dacx_lb.place(x=230, y=230)
        self.dacx_jg_bt = tk.Button(self.dacx_wd, text='按机构查询', font=('Arial', 12), width=20, height=2,
                                    command=self.dacx_jgcx_ui)
        self.dacx_jg_bt.place(x=400, y=150)
        self.dacx_zw_bt = tk.Button(self.dacx_wd, text='按个人信息查询', font=('Arial', 12), width=20, height=2,
                                    command=self.dacx_agrxxcx_ui)
        self.dacx_zw_bt.place(x=400, y=300)
        self.sb_fh_bt11 = tk.Button(self.dacx_wd, text='退出登录', font=('Arial', 8), width=10, height=1,
                                    command=self.fanhuidenglu)
        self.sb_fh_bt11.place(x=0, y=0)
        self.yw_fh_bt21 = tk.Button(self.dacx_wd, text='<<返回管理', font=('Arial', 8), width=10, height=1,
                                    command=self.fanhuiguanli)
        self.yw_fh_bt21.place(x=87, y=0)
        self.dacx_fh_bt = tk.Button(self.dacx_wd, text='<<返回档案业务', font=('Arial', 8), width=15, height=1,
                                    command=self.fanhuidangan)
        self.dacx_fh_bt.place(x=174, y=0)
        self.huanying = tk.Label(self.dacx_wd, text='欢迎您：', bg='white', fg='black', font=('Arial', 10), width=8,
                                 height=1)
        self.huanying.place(x=0, y=570)
        self.huanying1 = tk.Label(self.dacx_wd, text=self.admin, bg='white', fg='black', font=('Arial', 10), width=20,
                                  height=1)
        self.huanying1.place(x=60, y=570)

    # 档案查询按机构查询界面
    def dacx_jgcx_ui(self):
        self.dacx_jgcx_wd = tk.Tk()
        self.dacx_jgcx_wd.title('按机构信息查询档案')
        self.dacx_jgcx_wd.geometry('1000x600')

        self.ivar = tk.StringVar()
        self.dacx_jgcx_i_lb = tk.Label(self.dacx_jgcx_wd, text='1级机构', bg='white', fg='black', font=('Arial', 10),
                                       width=15, height=1)
        self.dacx_jgcx_i_lb.place(x=350, y=100)
        self.i_cb = ttk.Combobox(self.dacx_jgcx_wd, textvariable=self.ivar, width=25)  # 下拉表
        self.i_cb['values'] = uas.acc_sql_i()
        self.i_cb.bind("<<ComboboxSelected>>", self.ix_jg)
        self.i_cb.place(x=460, y=100)

        self.dacx_jgcx_ii_lb = tk.Label(self.dacx_jgcx_wd, text='2级机构', bg='white', fg='black', font=('Arial', 10),
                                        width=15, height=1)
        self.dacx_jgcx_ii_lb.place(x=350, y=160)
        self.ii_cb = ttk.Combobox(self.dacx_jgcx_wd, width=25)  # 下拉表
        self.ii_cb.bind("<<ComboboxSelected>>", self.iix_jg)
        self.ii_cb.place(x=460, y=160)

        self.dacx_jgcx_iii_lb = tk.Label(self.dacx_jgcx_wd, text='3级机构', bg='white', fg='black', font=('Arial', 10),
                                         width=15, height=1)
        self.dacx_jgcx_iii_lb.place(x=350, y=220)
        self.iii_cb = ttk.Combobox(self.dacx_jgcx_wd, width=25)  # 下拉表
        self.iii_cb.place(x=460, y=220)

        self.dacx_jgcx_zwfl_lb = tk.Label(self.dacx_jgcx_wd, text='职位分类', bg='white', fg='black', font=('Arial', 10),
                                          width=15, height=1)
        self.dacx_jgcx_zwfl_lb.place(x=350, y=280)
        self.zwfl_cb = ttk.Combobox(self.dacx_jgcx_wd, width=25)  # 下拉表
        self.zwfl_cb['values'] = ("员工", "设计")
        self.zwfl_cb.current(0)
        self.zwfl_cb.place(x=460, y=280)

        self.jgcx_bt = tk.Button(self.dacx_jgcx_wd, text='确认查询', font=('Arial', 12), width=30, height=2,
                                 command=self.jgcx_querenchaxun)
        self.jgcx_bt.place(x=350, y=450)
        self.text5 = tk.Label(self.dacx_jgcx_wd, text=' ')
        self.text5.place(x=0, y=540)

    # 档案查询个人信息输入界面
    def dacx_agrxxcx_ui(self):
        self.dacx_agrxxcx_wd = tk.Tk()
        self.dacx_agrxxcx_wd.title('按个人信息查询档案')
        self.dacx_agrxxcx_wd.geometry('1000x600')
        self.cxlb = 'wx'
        self.grxxcx_var = tk.StringVar()
        self.agrxxcx_en = tk.Entry(self.dacx_agrxxcx_wd, show=None, font=('Arial', 14), width=50)
        self.agrxxcx_en.place(x=220, y=156)  # zh_en.get()获得输入内容
        self.agrxxcx_rb1 = tk.Radiobutton(self.dacx_agrxxcx_wd, text='按编号', variable=self.grxxcx_var, value='bh',
                                          command=self.a1)  #
        self.agrxxcx_rb1.place(x=300, y=300)
        self.agrxxcx_rb2 = tk.Radiobutton(self.dacx_agrxxcx_wd, text='按姓名', variable=self.grxxcx_var, value='xm',
                                          command=self.a2)  #
        self.agrxxcx_rb2.place(x=500, y=300)
        self.agrxxcx_rb3 = tk.Radiobutton(self.dacx_agrxxcx_wd, text='按职位', variable=self.grxxcx_var, value='zw',
                                          command=self.a3)  #
        self.agrxxcx_rb3.place(x=300, y=350)
        self.agrxxcx_rb4 = tk.Radiobutton(self.dacx_agrxxcx_wd, text='按性别', variable=self.grxxcx_var, value='xb',
                                          command=self.a4)  #
        self.agrxxcx_rb4.place(x=500, y=350)
        self.agrxxcx_bt = tk.Button(self.dacx_agrxxcx_wd, text='确认查询', font=('Arial', 12), width=30, height=2,
                                    command=self.grxx_querenchaxun)
        self.agrxxcx_bt.place(x=290, y=450)
        self.text4 = tk.Label(self.dacx_agrxxcx_wd, text=' ')
        self.text4.place(x=0, y=540)

    # 个人信息简略显示界面
    def cxjg_jlxx_ui(self):
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

    # 档案录入界面
    def dalr_ui(self):
        self.today = datetime.date.today()
        self.today = str(self.today)
        self.darr_wd = tk.Tk()
        self.darr_wd.title('档案录入')
        self.darr_wd.geometry('1380x720')
        self.i_lb = tk.Label(self.darr_wd, text='1级机构', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.i_lb.place(x=0, y=2)

        self.ivar = tk.StringVar()
        self.i_cb = ttk.Combobox(self.darr_wd, textvariable=self.ivar, width=25)  # 下拉表
        self.i_cb['values'] = uas.acc_sql_i()
        self.i_cb.bind("<<ComboboxSelected>>", self.ix_jg)
        self.i_cb.place(x=110, y=1)

        self.ii_lb = tk.Label(self.darr_wd, text='2级机构', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.ii_lb.place(x=350, y=2)
        self.ii_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.ii_cb.bind("<<ComboboxSelected>>", self.iix_jg)
        self.ii_cb.place(x=460, y=1)

        self.iii_lb = tk.Label(self.darr_wd, text='3级机构', bg='white', fg='black', font=('Arial', 10), width=15,
                               height=1)
        self.iii_lb.place(x=700, y=2)
        self.iii_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.iii_cb.place(x=810, y=1)

        self.zwfl_lb = tk.Label(self.darr_wd, text='职位分类', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=1)
        self.zwfl_lb.place(x=0, y=30)
        self.zwfl_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.zwfl_cb['values'] = ("员工", "设计")
        self.zwfl_cb.current(0)
        self.zwfl_cb.place(x=110, y=30)

        self.zwmc_lb = tk.Label(self.darr_wd, text='职位名称', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=1)
        self.zwmc_lb.place(x=350, y=30)
        self.zwmc_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.zwmc_cb['values'] = ("普通员工", "ui设计", "外观设计")
        self.zwmc_cb.current(0)
        self.zwmc_cb.place(x=460, y=30)

        self.zc_lb = tk.Label(self.darr_wd, text='职称', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.zc_lb.place(x=700, y=30)
        self.zc_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.zc_cb['values'] = ("普通员工", "高级员工", "工程师", "设计师")
        self.zc_cb.current(0)
        self.zc_cb.place(x=810, y=30)

        self.xb_lb = tk.Label(self.darr_wd, text='性别', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.xb_lb.place(x=350, y=60)
        self.xb_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.xb_cb['values'] = ("男", "女")
        self.xb_cb.current(0)
        self.xb_cb.place(x=460, y=60)

        self.xm_lb = tk.Label(self.darr_wd, text='姓名', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.xm_lb.place(x=0, y=60)
        self.xm_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.xm_en.place(x=110, y=58)  # zh_en.get()获得输入内容

        self.em_lb = tk.Label(self.darr_wd, text='email', bg='white', fg='black', font=('Arial', 10), width=15,
                              height=1)
        self.em_lb.place(x=700, y=60)
        self.em_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.em_en.place(x=810, y=58)  # zh_en.get()获得输入内容

        self.dh_lb = tk.Label(self.darr_wd, text='电话', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.dh_lb.place(x=0, y=90)
        self.dh_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.dh_en.place(x=110, y=88)  # zh_en.get()获得输入内容

        self.qq_lb = tk.Label(self.darr_wd, text='QQ', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.qq_lb.place(x=350, y=90)
        self.qq_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.qq_en.place(x=460, y=88)  # zh_en.get()获得输入内容

        self.sj_lb = tk.Label(self.darr_wd, text='手机', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.sj_lb.place(x=700, y=90)
        self.sj_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.sj_en.place(x=810, y=88)  # zh_en.get()获得输入内容

        self.zz_lb = tk.Label(self.darr_wd, text='住址', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.zz_lb.place(x=0, y=120)
        self.zz_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=56)
        self.zz_en.place(x=110, y=118)  # zh_en.get()获得输入内容

        self.yb_lb = tk.Label(self.darr_wd, text='邮编', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.yb_lb.place(x=700, y=120)
        self.yb_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.yb_en.place(x=810, y=118)  # zh_en.get()获得输入内容

        self.gj_lb = tk.Label(self.darr_wd, text='国籍', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.gj_lb.place(x=0, y=150)
        self.gj_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.gj_cb['values'] = ("中国", "美国", "英国", "芬兰")
        self.gj_cb.current(0)
        self.gj_cb.place(x=110, y=148)

        self.zjxy_lb = tk.Label(self.darr_wd, text='宗教信仰', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=1)
        self.zjxy_lb.place(x=0, y=180)
        self.zjxy_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.zjxy_cb['values'] = ("佛", "无", "伊斯兰", "基督")
        self.zjxy_cb.current(0)
        self.zjxy_cb.place(x=110, y=178)

        self.xcbz_lb = tk.Label(self.darr_wd, text='薪酬标准', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=1)
        self.xcbz_lb.place(x=0, y=240)
        self.xcbz_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.xcbz_cb['values'] = ("员工", "经理", "其他")
        self.xcbz_cb.current(0)
        self.xcbz_cb.place(x=110, y=238)

        self.zzmm_lb = tk.Label(self.darr_wd, text='政治面貌', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=1)
        self.zzmm_lb.place(x=350, y=180)
        self.zzmm_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.zzmm_cb['values'] = ("群众", "共青团员", "共产党员")
        self.zzmm_cb.current(0)
        self.zzmm_cb.place(x=460, y=178)

        self.xl_lb = tk.Label(self.darr_wd, text='学历', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.xl_lb.place(x=350, y=210)
        self.xl_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.xl_cb['values'] = ("本科", "硕士", "博士", "其他")
        self.xl_cb.current(0)
        self.xl_cb.place(x=460, y=208)

        self.jynx_lb = tk.Label(self.darr_wd, text='教育年限', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=1)
        self.jynx_lb.place(x=700, y=210)
        self.jynx_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.jynx_cb['values'] = (9, 12, 16, 19, 21)
        self.jynx_cb.current(1)
        self.jynx_cb.place(x=810, y=208)

        self.tc_lb = tk.Label(self.darr_wd, text='特长', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.tc_lb.place(x=350, y=270)
        self.tc_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.tc_cb['values'] = ("python", "c", "c++", "数据库", "java", "ios")
        self.tc_cb.current(0)
        self.tc_cb.place(x=460, y=268)

        self.ah_lb = tk.Label(self.darr_wd, text='爱好', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.ah_lb.place(x=700, y=270)
        self.ah_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.ah_cb['values'] = ("音乐", "无", "绘画", "摄影", "舞蹈")
        self.ah_cb.current(0)
        self.ah_cb.place(x=810, y=268)

        self.mz_lb = tk.Label(self.darr_wd, text='民族', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.mz_lb.place(x=1050, y=150)
        self.mz_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.mz_cb['values'] = ("汉族", "维吾尔族", "苗族", "壮族")
        self.mz_cb.current(0)
        self.mz_cb.place(x=1160, y=148)

        self.xlzy_lb = tk.Label(self.darr_wd, text='学历专业', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=1)
        self.xlzy_lb.place(x=1050, y=210)
        self.xlzy_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.xlzy_cb['values'] = ("计算机", "音乐学", "软件", "其他")
        self.xlzy_cb.current(0)
        self.xlzy_cb.place(x=1160, y=208)

        self.csd_lb = tk.Label(self.darr_wd, text='出生地', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.csd_lb.place(x=350, y=150)
        self.csd_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.csd_en.place(x=460, y=148)  # zh_en.get()获得输入内容

        self.sr_lb = tk.Label(self.darr_wd, text='生日', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.sr_lb.place(x=700, y=150)
        self.sr_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.sr_en.place(x=810, y=148)  # zh_en.get()获得输入内容

        self.sbhm_lb = tk.Label(self.darr_wd, text='社保号码', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=1)
        self.sbhm_lb.place(x=1050, y=180)
        self.sbhm_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.sbhm_en.place(x=1160, y=178)  # zh_en.get()获得输入内容

        self.sfzh_lb = tk.Label(self.darr_wd, text='身份证号', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=1)
        self.sfzh_lb.place(x=700, y=180)
        self.sfzh_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.sfzh_en.place(x=810, y=178)  # zh_en.get()获得输入内容

        self.zh_lb = tk.Label(self.darr_wd, text='账号', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.zh_lb.place(x=700, y=240)
        self.zh_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.zh_en.place(x=810, y=238)  # zh_en.get()获得输入内容

        self.khh_lb = tk.Label(self.darr_wd, text='开户行', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.khh_lb.place(x=350, y=240)
        self.khh_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.khh_en.place(x=460, y=238)  # zh_en.get()获得输入内容

        self.nl_lb = tk.Label(self.darr_wd, text='年龄', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.nl_lb.place(x=0, y=210)
        self.nl_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.nl_en.place(x=110, y=208)  # zh_en.get()获得输入内容

        self.jdsj_lb = tk.Label(self.darr_wd, text='建档时间', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=1)
        self.jdsj_lb.place(x=0, y=270)
        self.jdsj_lb = tk.Label(self.darr_wd, text=self.today, bg='white', fg='black', font=('Arial', 10), width=30,
                                height=1)
        self.jdsj_lb.place(x=110, y=270)

        self.djr_lb = tk.Label(self.darr_wd, text='登记人', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.djr_lb.place(x=1050, y=240)
        self.djr_lb = tk.Label(self.darr_wd, text=self.admin[0], bg='white', fg='black', font=('Arial', 10), width=30,
                               height=1)
        self.djr_lb.place(x=1160, y=240)

        self.grll_lb = tk.Label(self.darr_wd, text='个人履历', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=7)
        self.grll_lb.place(x=0, y=300)
        self.grll_tx = tk.Text(self.darr_wd, width=157, height=7)
        self.grll_tx.place(x=110, y=298)

        self.jtgx_lb = tk.Label(self.darr_wd, text='家庭关系', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=7)
        self.jtgx_lb.place(x=0, y=440)
        self.jtgx_tx = tk.Text(self.darr_wd, width=157, height=7)
        self.jtgx_tx.place(x=110, y=438)

        self.bz_lb = tk.Label(self.darr_wd, text='备注', bg='white', fg='black', font=('Arial', 10), width=15, height=7)
        self.bz_lb.place(x=0, y=580)
        self.bz_tx = tk.Text(self.darr_wd, width=157, height=7)
        self.bz_tx.place(x=110, y=578)

        self.tx_lb = tk.Label(self.darr_wd, text='照片', bg='white', fg='black', font=('Arial', 10), width=18, height=8)
        self.tx_lb.place(x=1050, y=2)

        self.qr_bt = tk.Button(self.darr_wd, text='确认', font=('Arial', 12), width=10, height=1, command=self.queren)
        self.qr_bt.place(x=1240, y=20)
        self.qc_bt = tk.Button(self.darr_wd, text='清除', font=('Arial', 12), width=10, height=1, command=self.qingchu)
        self.qc_bt.place(x=1240, y=60)

    # 档案复核界面
    def dafh_ui(self, fhxx):
        self.darr_wd = tk.Tk()
        self.darr_wd.title('档案详情')
        self.darr_wd.geometry('1380x720')
        self.i_lb = tk.Label(self.darr_wd, text='1级机构', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.i_lb.place(x=0, y=2)
        self.i_clb = tk.Label(self.darr_wd, text=fhxx[2], bg='white', fg='black', font=('Arial', 10), width=30,
                              height=1)
        self.i_clb.place(x=110, y=2)

        self.ii_lb = tk.Label(self.darr_wd, text='2级机构', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.ii_lb.place(x=350, y=2)
        self.ii_clb = tk.Label(self.darr_wd, text=fhxx[3], bg='white', fg='black', font=('Arial', 10), width=30,
                               height=1)
        self.ii_clb.place(x=460, y=2)

        self.iii_lb = tk.Label(self.darr_wd, text='3级机构', bg='white', fg='black', font=('Arial', 10), width=15,
                               height=1)
        self.iii_lb.place(x=700, y=2)
        self.iii_clb = tk.Label(self.darr_wd, text=fhxx[4], bg='white', fg='black', font=('Arial', 10), width=30,
                                height=1)
        self.iii_clb.place(x=810, y=2)

        self.zwfl_lb = tk.Label(self.darr_wd, text='职位分类', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=1)
        self.zwfl_lb.place(x=0, y=30)
        self.zwfl_clb = tk.Label(self.darr_wd, text=fhxx[5], bg='white', fg='black', font=('Arial', 10), width=30,
                                 height=1)
        self.zwfl_clb.place(x=110, y=30)

        self.zwmc_lb = tk.Label(self.darr_wd, text='职位名称', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=1)
        self.zwmc_lb.place(x=350, y=30)
        self.zwmc_clb = tk.Label(self.darr_wd, text=fhxx[6], bg='white', fg='black', font=('Arial', 10), width=30,
                                 height=1)
        self.zwmc_clb.place(x=460, y=30)

        self.zc_lb = tk.Label(self.darr_wd, text='职称', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.zc_lb.place(x=700, y=30)
        self.zc_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.xiala_index = ["普通员工", "高级员工", "工程师", "设计师"]
        self.zc_cb['values'] = self.xiala_index
        self.zc_cb.current(self.xiala_index.index(fhxx[7]))
        self.zc_cb.place(x=810, y=30)

        self.xb_lb = tk.Label(self.darr_wd, text='性别', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.xb_lb.place(x=350, y=60)
        self.xb_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.xiala_index = ["男", "女"]
        self.xb_cb['values'] = self.xiala_index
        self.xb_cb.current(self.xiala_index.index(fhxx[9]))
        self.xb_cb.place(x=460, y=60)

        self.xm_lb = tk.Label(self.darr_wd, text='姓名', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.xm_lb.place(x=0, y=60)
        self.xm_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.xm_en.insert(END, fhxx[8])
        self.xm_en.place(x=110, y=58)  # zh_en.get()获得输入内容

        self.em_lb = tk.Label(self.darr_wd, text='email', bg='white', fg='black', font=('Arial', 10), width=15,
                              height=1)
        self.em_lb.place(x=700, y=60)
        self.em_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.em_en.insert(END, fhxx[10])
        self.em_en.place(x=810, y=58)  # zh_en.get()获得输入内容

        self.dh_lb = tk.Label(self.darr_wd, text='电话', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.dh_lb.place(x=0, y=90)
        self.dh_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.dh_en.insert(END, fhxx[11])
        self.dh_en.place(x=110, y=88)  # zh_en.get()获得输入内容

        self.qq_lb = tk.Label(self.darr_wd, text='QQ', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.qq_lb.place(x=350, y=90)
        self.qq_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.qq_en.insert(END, fhxx[12])
        self.qq_en.place(x=460, y=88)  # zh_en.get()获得输入内容

        self.sj_lb = tk.Label(self.darr_wd, text='手机', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.sj_lb.place(x=700, y=90)
        self.sj_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.sj_en.insert(END, fhxx[13])
        self.sj_en.place(x=810, y=88)  # zh_en.get()获得输入内容

        self.zz_lb = tk.Label(self.darr_wd, text='住址', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.zz_lb.place(x=0, y=120)
        self.zz_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=56)
        self.zz_en.insert(END, fhxx[14])
        self.zz_en.place(x=110, y=118)  # zh_en.get()获得输入内容

        self.yb_lb = tk.Label(self.darr_wd, text='邮编', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.yb_lb.place(x=700, y=120)
        self.yb_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.yb_en.insert(END, fhxx[15])
        self.yb_en.place(x=810, y=118)  # zh_en.get()获得输入内容

        self.gj_lb = tk.Label(self.darr_wd, text='国籍', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.gj_lb.place(x=0, y=150)
        self.gj_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.xiala_index = ["中国", "美国", "英国", "芬兰"]
        self.gj_cb['values'] = self.xiala_index
        self.gj_cb.current(self.xiala_index.index(fhxx[16]))
        self.gj_cb.place(x=110, y=148)

        self.zjxy_lb = tk.Label(self.darr_wd, text='宗教信仰', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=1)
        self.zjxy_lb.place(x=0, y=180)
        self.zjxy_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.xiala_index = ["佛", "无", "伊斯兰", "基督"]
        self.zjxy_cb['values'] = self.xiala_index
        self.zjxy_cb.current(self.xiala_index.index(fhxx[20]))
        self.zjxy_cb.place(x=110, y=178)

        self.xcbz_lb = tk.Label(self.darr_wd, text='薪酬标准', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=1)
        self.xcbz_lb.place(x=0, y=240)
        self.xcbz_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.xiala_index = ["员工", "经理", "其他"]
        self.xcbz_cb['values'] = self.xiala_index
        self.xcbz_cb.current(self.xiala_index.index(fhxx[28]))
        self.xcbz_cb.place(x=110, y=238)

        self.zzmm_lb = tk.Label(self.darr_wd, text='政治面貌', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=1)
        self.zzmm_lb.place(x=350, y=180)
        self.zzmm_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.xiala_index = ["群众", "共青团员", "共产党员"]
        self.zzmm_cb['values'] = self.xiala_index
        self.zzmm_cb.current(self.xiala_index.index(fhxx[21]))
        self.zzmm_cb.place(x=460, y=178)

        self.xl_lb = tk.Label(self.darr_wd, text='学历', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.xl_lb.place(x=350, y=210)
        self.xl_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.xiala_index = ["本科", "硕士", "博士", "其他"]
        self.xl_cb['values'] = self.xiala_index
        self.xl_cb.current(self.xiala_index.index(fhxx[25]))
        self.xl_cb.place(x=460, y=208)

        self.jynx_lb = tk.Label(self.darr_wd, text='教育年限', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=1)
        self.jynx_lb.place(x=700, y=210)
        self.jynx_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.xiala_index = [9, 12, 16, 19, 21]
        self.jynx_cb['values'] = self.xiala_index
        self.jynx_cb.current(self.xiala_index.index(fhxx[26]))
        self.jynx_cb.place(x=810, y=208)

        self.tc_lb = tk.Label(self.darr_wd, text='特长', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.tc_lb.place(x=350, y=270)
        self.tc_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.xiala_index = ["python", "c", "c++", "数据库", "java", "ios"]
        self.tc_cb['values'] = self.xiala_index
        self.tc_cb.current(self.xiala_index.index(fhxx[33]))
        self.tc_cb.place(x=460, y=268)

        self.ah_lb = tk.Label(self.darr_wd, text='爱好', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.ah_lb.place(x=700, y=270)
        self.ah_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.xiala_index = ["音乐", "无", "绘画", "摄影", "舞蹈"]
        self.ah_cb['values'] = self.xiala_index
        self.ah_cb.current(self.xiala_index.index(fhxx[34]))
        self.ah_cb.place(x=810, y=268)

        self.mz_lb = tk.Label(self.darr_wd, text='民族', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.mz_lb.place(x=1050, y=150)
        self.mz_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.xiala_index = ["汉族", "维吾尔族", "苗族", "壮族"]
        self.mz_cb['values'] = self.xiala_index
        self.mz_cb.current(self.xiala_index.index(fhxx[19]))
        self.mz_cb.place(x=1160, y=148)

        self.xlzy_lb = tk.Label(self.darr_wd, text='学历专业', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=1)
        self.xlzy_lb.place(x=1050, y=210)
        self.xlzy_cb = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.xiala_index = ["计算机", "音乐学", "软件", "其他"]
        self.xlzy_cb['values'] = self.xiala_index
        self.xlzy_cb.current(self.xiala_index.index(fhxx[27]))
        self.xlzy_cb.place(x=1160, y=208)

        self.csd_lb = tk.Label(self.darr_wd, text='出生地', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.csd_lb.place(x=350, y=150)
        self.csd_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.csd_en.insert(END, fhxx[17])
        self.csd_en.place(x=460, y=148)  # zh_en.get()获得输入内容

        self.sr_lb = tk.Label(self.darr_wd, text='生日', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.sr_lb.place(x=700, y=150)
        self.sr_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.sr_en.insert(END, fhxx[18])
        self.sr_en.place(x=810, y=148)  # zh_en.get()获得输入内容

        self.sbhm_lb = tk.Label(self.darr_wd, text='社保号码', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=1)
        self.sbhm_lb.place(x=1050, y=180)
        self.sbhm_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.sbhm_en.insert(END, fhxx[23])
        self.sbhm_en.place(x=1160, y=178)  # zh_en.get()获得输入内容

        self.sfzh_lb = tk.Label(self.darr_wd, text='身份证号', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=1)
        self.sfzh_lb.place(x=700, y=180)
        self.sfzh_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.sfzh_en.insert(END, fhxx[22])
        self.sfzh_en.place(x=810, y=178)  # zh_en.get()获得输入内容

        self.zh_lb = tk.Label(self.darr_wd, text='账号', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.zh_lb.place(x=700, y=240)
        self.zh_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.zh_en.insert(END, fhxx[30])
        self.zh_en.place(x=810, y=238)  # zh_en.get()获得输入内容

        self.khh_lb = tk.Label(self.darr_wd, text='开户行', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.khh_lb.place(x=350, y=240)
        self.khh_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.khh_en.insert(END, fhxx[29])
        self.khh_en.place(x=460, y=238)  # zh_en.get()获得输入内容

        self.nl_lb = tk.Label(self.darr_wd, text='年龄', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.nl_lb.place(x=0, y=210)
        self.nl_en = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.nl_en.insert(END, fhxx[24])
        self.nl_en.place(x=110, y=208)  # zh_en.get()获得输入内容

        self.jdsj_lb = tk.Label(self.darr_wd, text='建档时间', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=1)
        self.jdsj_lb.place(x=0, y=270)
        self.jdsj_lb = tk.Label(self.darr_wd, text=fhxx[32], bg='white', fg='black', font=('Arial', 10), width=30,
                                height=1)
        self.jdsj_lb.place(x=110, y=270)

        self.djr_lb = tk.Label(self.darr_wd, text='登记人', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.djr_lb.place(x=1050, y=240)
        self.djr_lb = tk.Label(self.darr_wd, text=fhxx[31], bg='white', fg='black', font=('Arial', 10), width=30,
                               height=1)
        self.djr_lb.place(x=1160, y=240)

        self.djr_lb = tk.Label(self.darr_wd, text='档案编号', bg='white', fg='black', font=('Arial', 10), width=15,
                               height=1)
        self.djr_lb.place(x=1050, y=270)
        self.djr_lb = tk.Label(self.darr_wd, text=fhxx[1], bg='white', fg='black', font=('Arial', 10), width=30,
                               height=1)
        self.djr_lb.place(x=1160, y=270)

        self.grll_lb = tk.Label(self.darr_wd, text='个人履历', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=7)
        self.grll_lb.place(x=0, y=300)
        self.grll_tx = tk.Text(self.darr_wd, width=157, height=7)
        self.grll_tx.insert(INSERT, fhxx[35])
        self.grll_tx.place(x=110, y=298)

        self.jtgx_lb = tk.Label(self.darr_wd, text='家庭关系', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=7)
        self.jtgx_lb.place(x=0, y=440)
        self.jtgx_tx = tk.Text(self.darr_wd, width=157, height=7)
        self.jtgx_tx.insert(INSERT, fhxx[36])
        self.jtgx_tx.place(x=110, y=438)

        self.bz_lb = tk.Label(self.darr_wd, text='备注', bg='white', fg='black', font=('Arial', 10), width=15, height=7)
        self.bz_lb.place(x=0, y=580)
        self.bz_tx = tk.Text(self.darr_wd, width=157, height=7)
        self.bz_tx.insert(INSERT, fhxx[37])
        self.bz_tx.place(x=110, y=578)

        self.tx_lb = tk.Label(self.darr_wd, text='照片', bg='white', fg='black', font=('Arial', 10), width=18, height=8)
        self.tx_lb.place(x=1050, y=2)
        self.fhjg = fhxx
        if self.admin[1] == '人事经理':
            if fhxx[-1] == '待审核':
                self.qr_bt = tk.Button(self.darr_wd, text='通过审核', font=('Arial', 12), width=10, height=1,
                                       command=self.tgsh)
                self.qr_bt.place(x=1240, y=20)
            elif fhxx[-1] == '归档':
                self.qr_bt = tk.Button(self.darr_wd, text='提交修改', font=('Arial', 12), width=10, height=1,
                                       command=self.tjxg)
                self.qr_bt.place(x=1240, y=20)
            if fhxx[-1] != '已删除':
                self.sc_bt = tk.Button(self.darr_wd, text='删除该档', font=('Arial', 12), width=10, height=1,
                                       command=self.scgd)
                self.sc_bt.place(x=1240, y=100)
        else:
            self.qr_bt = tk.Button(self.darr_wd, text='提交修改', font=('Arial', 12), width=10, height=1, command=self.tjxg)
            self.qr_bt.place(x=1240, y=20)
        self.qc_bt = tk.Button(self.darr_wd, text='恢复修改', font=('Arial', 12), width=10, height=1,
                               command=self.dashxg_hf)
        self.qc_bt.place(x=1240, y=60)

    # 薪酬标准录入界面
    def xclr_ui(self):
        self.today = datetime.date.today()
        self.today = str(self.today)
        self.darr_wd = tk.Tk()
        self.darr_wd.title('薪酬标准录入')
        self.darr_wd.geometry('1380x720')
        self.ab = tk.Label(self.darr_wd, text='薪酬标准编号', bg='white', fg='black', font=('Arial', 10), width=15,
                           height=1)
        self.ab.place(x=0, y=2)

        self.ivar = tk.StringVar()
        self.aa = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.aa.place(x=110, y=1)  # zh_en.get()获得输入内容

        self.ii_lb = tk.Label(self.darr_wd, text='薪酬标准名称', bg='white', fg='black', font=('Arial', 10), width=15,
                              height=1)
        self.ii_lb.place(x=350, y=2)
        self.bb = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.bb.place(x=460, y=1)

        self.iii_lb = tk.Label(self.darr_wd, text='制定人', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.iii_lb.place(x=700, y=2)
        self.cc = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.cc.place(x=810, y=1)

        self.zwfl_lb = tk.Label(self.darr_wd, text='登记时间', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=1)
        self.zwfl_lb.place(x=0, y=30)
        self.dd = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.dd.place(x=110, y=30)

        self.zwmc_lb = tk.Label(self.darr_wd, text='职位名称', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=1)
        self.zwmc_lb.place(x=350, y=30)
        self.ee = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.ee.place(x=460, y=30)

        self.zc_lb = tk.Label(self.darr_wd, text='基本工资', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.zc_lb.place(x=700, y=30)
        self.ff = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.ff.place(x=810, y=30)

        self.xb_lb = tk.Label(self.darr_wd, text='养老保险', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.xb_lb.place(x=350, y=60)
        self.gg = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.gg.place(x=460, y=60)

        self.xm_lb = tk.Label(self.darr_wd, text='医疗保险', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.xm_lb.place(x=0, y=60)
        self.hh = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.hh.place(x=110, y=58)  # zh_en.get()获得输入内容

        self.em_lb = tk.Label(self.darr_wd, text='失业保险', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.em_lb.place(x=700, y=60)
        self.jj = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.jj.place(x=810, y=58)  # zh_en.get()获得输入内容

        self.dh_lb = tk.Label(self.darr_wd, text='住房公积金', bg='white', fg='black', font=('Arial', 10), width=15,
                              height=1)
        self.dh_lb.place(x=0, y=90)
        self.kk = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.kk.place(x=110, y=88)  # zh_en.get()获得输入内容

        self.qq_lb = tk.Label(self.darr_wd, text='状态', bg='white', fg='black', font=('Arial', 10), width=15, height=1)
        self.qq_lb.place(x=350, y=90)
        self.ll = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.xiala_index = ["复核", "已复核"]
        self.ll['values'] = self.xiala_index
        self.ll.place(x=460, y=88)  # zh_en.get()获得输入内容
        self.qr_bt = tk.Button(self.darr_wd, text='确认', font=('Arial', 12), width=10, height=1,
                               command=self.queren_xc)
        self.qr_bt.place(x=1240, y=20)
        self.qc_bt = tk.Button(self.darr_wd, text='清除', font=('Arial', 12), width=10, height=1, command=self.xcxz_ui)
        self.qc_bt.place(x=1240, y=60)

    # 员工薪酬登记表
    def ygxclr_ui(self):
        self.today = datetime.date.today()
        self.today = str(self.today)
        self.darr_wd = tk.Tk()
        self.darr_wd.title('员工薪酬登记')
        self.darr_wd.geometry('1380x720')
        self.i_lb = tk.Label(self.darr_wd, text='员工编号', bg='white', fg='black', font=('Arial', 10), width=15,
                             height=1)
        self.i_lb.place(x=0, y=2)

        self.ivar = tk.StringVar()
        self.aaa = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.aaa.place(x=110, y=1)  # zh_en.get()获得输入内容

        self.ii_lb = tk.Label(self.darr_wd, text='奖励奖金', bg='white', fg='black', font=('Arial', 10), width=15,
                              height=1)
        self.ii_lb.place(x=350, y=2)
        self.bbb = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.bbb.place(x=460, y=1)

        self.iii_lb = tk.Label(self.darr_wd, text='扣除奖金', bg='white', fg='black', font=('Arial', 10), width=15,
                               height=1)
        self.iii_lb.place(x=700, y=2)
        self.ccc = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.ccc.place(x=810, y=1)

        self.zwfl_lb = tk.Label(self.darr_wd, text='应发放总额', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=1)
        self.zwfl_lb.place(x=0, y=30)
        self.ddd = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.ddd.place(x=110, y=30)

        self.zwmc_lb = tk.Label(self.darr_wd, text='薪酬标准编号', bg='white', fg='black', font=('Arial', 10), width=15,
                                height=1)
        self.zwmc_lb.place(x=350, y=30)
        self.eee = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.eee.place(x=460, y=30)

        self.zc_lb = tk.Label(self.darr_wd, text='登记人', bg='white', fg='black', font=('Arial', 10), width=15,
                              height=1)
        self.zc_lb.place(x=700, y=30)
        self.fff = tk.Entry(self.darr_wd, show=None, font=('Arial', 14), width=21)
        self.fff.place(x=810, y=30)

        self.xb_lb = tk.Label(self.darr_wd, text='状态', bg='white', fg='black', font=('Arial', 10), width=15,
                              height=1)
        self.xb_lb.place(x=350, y=60)
        self.ggg = ttk.Combobox(self.darr_wd, width=25)  # 下拉表
        self.xiala_index = ["待登记", "待复核", "待发放"]
        self.ggg['values'] = self.xiala_index
        self.ggg.place(x=460, y=60)
        self.qr_bt = tk.Button(self.darr_wd, text='确认', font=('Arial', 12), width=10, height=1,
                               command=self.queren_ygxc)
        self.qr_bt.place(x=1240, y=20)
        self.qc_bt = tk.Button(self.darr_wd, text='清除', font=('Arial', 12), width=10, height=1, command=self.ygxclr_ui)
        self.qc_bt.place(x=1240, y=60)

    # 薪酬审核
    def xcshxz_ui(self):
        try:
            self.sb_wd.destroy()
        except:
            pass
        self.dayw_wd = tk.Tk()
        self.dayw_wd.title('选择功能')
        self.dayw_wd.geometry('1000x600')
        self.yw_lb = tk.Label(self.dayw_wd, text='选择审核功能：', bg='white', fg='black', font=('Arial', 15), width=12,
                              height=2)
        self.yw_lb.place(x=230, y=230)
        self.yw_cx_bt = tk.Button(self.dayw_wd, text='审核薪酬标准', font=('Arial', 12), width=20, height=2,
                                  command=self.xcbz)
        self.yw_cx_bt.place(x=400, y=150)
        self.yw_lr_bt = tk.Button(self.dayw_wd, text='审核员工薪酬', font=('Arial', 12), width=20, height=2,
                                  command=self.ygxcsh)
        self.yw_lr_bt.place(x=400, y=225)
        self.yw_fh_bt2 = tk.Button(self.dayw_wd, text='<<返回选择', font=('Arial', 8), width=10, height=1,
                                   command=self.xcxz_ui)
        self.yw_fh_bt2.place(x=87, y=0)
        self.huanying = tk.Label(self.dayw_wd, text='欢迎您：', bg='white', fg='black', font=('Arial', 10), width=8,
                                 height=1)
        self.huanying.place(x=0, y=570)
        self.huanying1 = tk.Label(self.dayw_wd, text=self.admin, bg='white', fg='black', font=('Arial', 10), width=20,
                                  height=1)
        self.huanying1.place(x=60, y=570)
        self.text3 = tk.Label(self.dayw_wd, text=' ')
        self.text3.place(x=0, y=540)

    # 薪酬业务选择界面
    def xcxz_ui(self):
        try:
            self.sb_wd.destroy()
        except:
            pass
        self.dayw_wd = tk.Tk()
        self.dayw_wd.title('选择薪酬业务')
        self.dayw_wd.geometry('1000x600')
        self.yw_lb = tk.Label(self.dayw_wd, text='选择薪酬业务：', bg='white', fg='black', font=('Arial', 15), width=12,
                              height=2)
        self.yw_lb.place(x=230, y=230)
        self.yw_cx_bt = tk.Button(self.dayw_wd, text='薪酬项目登记', font=('Arial', 12), width=20, height=2,
                                  command=self.xclr_ui)
        self.yw_cx_bt.place(x=400, y=150)
        self.yw_lr_bt = tk.Button(self.dayw_wd, text='员工薪酬登记', font=('Arial', 12), width=20, height=2,
                                  command=self.ygxclr_ui)
        self.yw_lr_bt.place(x=400, y=225)
        self.yw_sh_bt = tk.Button(self.dayw_wd, text='薪酬审核', font=('Arial', 12), width=20, height=2,
                                  command=self.xcshxz_ui)
        self.yw_sh_bt.place(x=400, y=300)
        self.yw_fh_bt2 = tk.Button(self.dayw_wd, text='<<返回选择', font=('Arial', 8), width=10, height=1,
                                   command=self.fanhuiguanli)
        self.yw_fh_bt2.place(x=87, y=0)
        self.huanying = tk.Label(self.dayw_wd, text='欢迎您：', bg='white', fg='black', font=('Arial', 10), width=8,
                                 height=1)
        self.huanying.place(x=0, y=570)
        self.huanying1 = tk.Label(self.dayw_wd, text=self.admin, bg='white', fg='black', font=('Arial', 10), width=20,
                                  height=1)
        self.huanying1.place(x=60, y=570)
        self.text3 = tk.Label(self.dayw_wd, text=' ')
        self.text3.place(x=0, y=540)

    # 员工薪酬审核ui
    def ygxcsh_ui(self):
        self.cxjg_jlxx_wd = tk.Tk()
        self.cxjg_jlxx_wd.title('信息摘要')
        self.cxjg_jlxx_wd.geometry('1200x600')
        self.biaotou = tk.Label(self.cxjg_jlxx_wd,
                                text='---员工编号---奖励奖金---扣除奖金---应付总额---薪酬标准编号---登记人---状态',
                                bg='white', fg='black', font=('Arial', 13), width=120, height=1)
        self.biaotou.place(x=4, y=2)
        self.jlxx_text = Text(self.cxjg_jlxx_wd, width=200, height=33)
        self.jlxx_text.place(x=0, y=30)
        self.biaotou2 = tk.Label(self.cxjg_jlxx_wd, text='本表仅显示查询前十条信息', bg='white', fg='black', font=('Arial', 15),
                                 width=90, height=1)
        self.biaotou2.place(x=1, y=500)
        self.jlxx_ind = -1

        if len(self.cxjg) >= 1:
            self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(8, self.cxjg[0][0]) + self.bkg(8, self.cxjg[0][
                1]) + '        ' + self.bkg(8,
                                            self.cxjg[
                                                0][
                                                2]) + '        ' + self.bkg(
                8, self.cxjg[0][3]) + '        ' + self.bkg(8, self.cxjg[0][4]) + '        ' + self.bkg(8,
                                                                                                        self.cxjg[0][
                                                                                                            5]) + '        ' + self.bkg(
                8, self.cxjg[0][6]) + '\n\n')
            self.jlxx_text.tag_add('link1', '1.5', '1.7')
            self.jlxx_text.tag_config('link1', foreground='green', underline=True)
            self.jlxx_text.tag_bind('link1', '<Button-1>', self.click1)
        if len(self.cxjg) >= 2:
            self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(8, self.cxjg[1][0]) + self.bkg(8, self.cxjg[1][
                1]) + '        ' + self.bkg(8,
                                            self.cxjg[
                                                1][
                                                2]) + '        ' + self.bkg(
                8, self.cxjg[1][3]) + '        ' + self.bkg(8, self.cxjg[1][4]) + '        ' + self.bkg(8,
                                                                                                        self.cxjg[1][
                                                                                                            5]) + '        ' + self.bkg(
                8, self.cxjg[1][6]) + '\n\n')
            self.jlxx_text.tag_add('link2', '3.5', '3.7')
            self.jlxx_text.tag_config('link2', foreground='green', underline=True)
            self.jlxx_text.tag_bind('link2', '<Button-1>', self.click2)
        if len(self.cxjg) >= 3:
            self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(8, self.cxjg[2][0]) + self.bkg(8, self.cxjg[2][
                1]) + '        ' + self.bkg(8,
                                            self.cxjg[
                                                2][
                                                2]) + '        ' + self.bkg(
                8, self.cxjg[2][3]) + '        ' + self.bkg(8, self.cxjg[2][4]) + '        ' + self.bkg(8,
                                                                                                        self.cxjg[2][
                                                                                                            5]) + '        ' + self.bkg(
                8, self.cxjg[2][6])+ '\n\n')
            self.jlxx_text.tag_add('link3', '5.5', '5.7')
            self.jlxx_text.tag_config('link3', foreground='green', underline=True)
            self.jlxx_text.tag_bind('link3', '<Button-1>', self.click3)
        if len(self.cxjg) >= 4:
            self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(8, self.cxjg[3][0]) + self.bkg(8, self.cxjg[3][
                1]) + '        ' + self.bkg(8,
                                            self.cxjg[
                                                3][
                                                2]) + '        ' + self.bkg(
                8, self.cxjg[3][3]) + '        ' + self.bkg(8, self.cxjg[3][4]) + '        ' + self.bkg(8,
                                                                                                        self.cxjg[3][
                                                                                                            5]) + '        ' + self.bkg(
                8, self.cxjg[3][6]) + '\n\n')
            self.jlxx_text.tag_add('link4', '7.5', '7.7')
            self.jlxx_text.tag_config('link4', foreground='green', underline=True)
            self.jlxx_text.tag_bind('link4', '<Button-1>', self.click4)
        if len(self.cxjg) >= 5:
            self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(8, self.cxjg[4][0]) + self.bkg(8, self.cxjg[4][
                1]) + '        ' + self.bkg(8,
                                            self.cxjg[
                                                4][
                                                2]) + '        ' + self.bkg(
                8, self.cxjg[4][3]) + '        ' + self.bkg(8, self.cxjg[4][4]) + '        ' + self.bkg(8,
                                                                                                        self.cxjg[4][
                                                                                                            5]) + '        ' + self.bkg(
                8, self.cxjg[4][6])  + '\n\n')
            self.jlxx_text.tag_add('link5', '9.5', '9.7')
            self.jlxx_text.tag_config('link5', foreground='green', underline=True)
            self.jlxx_text.tag_bind('link5', '<Button-1>', self.click5)
        if len(self.cxjg) >= 6:
            self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(8, self.cxjg[5][0]) + self.bkg(8, self.cxjg[5][
                1]) + '        ' + self.bkg(8,
                                            self.cxjg[
                                                5][
                                                2]) + '        ' + self.bkg(
                8, self.cxjg[5][3]) + '        ' + self.bkg(8, self.cxjg[5][4]) + '        ' + self.bkg(8,
                                                                                                        self.cxjg[5][
                                                                                                            5]) + '        ' + self.bkg(
                8, self.cxjg[5][6])  + '\n\n')
            self.jlxx_text.tag_add('link6', '11.5', '11.7')
            self.jlxx_text.tag_config('link6', foreground='green', underline=True)
            self.jlxx_text.tag_bind('link6', '<Button-1>', self.click6)
        if len(self.cxjg) >= 7:
            self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(8, self.cxjg[6][0]) + self.bkg(8, self.cxjg[6][
                1]) + '        ' + self.bkg(8,
                                            self.cxjg[
                                                6][
                                                2]) + '        ' + self.bkg(
                8, self.cxjg[6][3]) + '        ' + self.bkg(8, self.cxjg[6][4]) + '        ' + self.bkg(8,
                                                                                                        self.cxjg[6][
                                                                                                            5]) + '        ' + self.bkg(
                8, self.cxjg[6][6])  + '\n\n')
            self.jlxx_text.tag_add('link7', '13.5', '13.7')
            self.jlxx_text.tag_config('link7', foreground='green', underline=True)
            self.jlxx_text.tag_bind('link7', '<Button-1>', self.click7)
        if len(self.cxjg) >= 8:
            self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(8, self.cxjg[7][0]) + self.bkg(8, self.cxjg[7][
                1]) + '        ' + self.bkg(8,
                                            self.cxjg[
                                                7][
                                                2]) + '        ' + self.bkg(
                8, self.cxjg[7][3]) + '        ' + self.bkg(8, self.cxjg[7][4]) + '        ' + self.bkg(8,
                                                                                                        self.cxjg[7][
                                                                                                            5]) + '        ' + self.bkg(
                8, self.cxjg[7][6])  + '\n\n')
            self.jlxx_text.tag_add('link8', '15.5', '15.7')
            self.jlxx_text.tag_config('link8', foreground='green', underline=True)
            self.jlxx_text.tag_bind('link8', '<Button-1>', self.click8)
        if len(self.cxjg) >= 9:
            self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(8, self.cxjg[8][0]) + self.bkg(8, self.cxjg[8][
                1]) + '        ' + self.bkg(8,
                                            self.cxjg[
                                                8][
                                                2]) + '        ' + self.bkg(
                8, self.cxjg[8][3]) + '        ' + self.bkg(8, self.cxjg[8][4]) + '        ' + self.bkg(8,
                                                                                                        self.cxjg[8][
                                                                                                            5]) + '        ' + self.bkg(
                8, self.cxjg[8][6]) + '\n\n')
            self.jlxx_text.tag_add('link9', '17.5', '17.7')
            self.jlxx_text.tag_config('link9', foreground='green', underline=True)
            self.jlxx_text.tag_bind('link9', '<Button-1>', self.click9)
        if len(self.cxjg) >= 19:
            self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(8, self.cxjg[9][0]) + self.bkg(8, self.cxjg[9][
                1]) + '        ' + self.bkg(8,
                                            self.cxjg[
                                                9][
                                                2]) + '        ' + self.bkg(
                8, self.cxjg[9][3]) + '        ' + self.bkg(8, self.cxjg[9][4]) + '        ' + self.bkg(8,
                                                                                                        self.cxjg[9][
                                                                                                            5]) + '        ' + self.bkg(
                8, self.cxjg[9][6]) + '\n\n')
            self.jlxx_text.tag_add('link10', '19.5', '19.7')
            self.jlxx_text.tag_config('link10', foreground='green', underline=True)
            self.jlxx_text.tag_bind('link10', '<Button-1>', self.click10)
        self.jlxx_text.config(state=DISABLED)

    # 员工审核ui
    def xcbzsh_ui(self):
        self.cxjg_jlxx_wd = tk.Tk()
        self.cxjg_jlxx_wd.title('信息摘要')
        self.cxjg_jlxx_wd.geometry('1200x600')
        self.biaotou = tk.Label(self.cxjg_jlxx_wd,
                                text='---薪酬标准编号---薪酬标准名称---制订人---登记时间---职位名称---基本工资---医疗保险---养老保险---失业保险---住房公积金---状态',
                                bg='white', fg='black', font=('Arial', 13), width=120, height=1)
        self.biaotou.place(x=4, y=2)
        self.jlxx_text = Text(self.cxjg_jlxx_wd, width=200, height=33)
        self.jlxx_text.place(x=0, y=30)
        self.biaotou2 = tk.Label(self.cxjg_jlxx_wd, text='本表仅显示查询前十条信息', bg='white', fg='black', font=('Arial', 15),
                                 width=90, height=1)
        self.biaotou2.place(x=1, y=500)
        self.jlxx_ind = -1

        if len(self.cxjg) >= 1:
            self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(8, self.cxjg[0][0]) + self.bkg(8, self.cxjg[0][
                1]) + '        ' + self.bkg(8,
                                            self.cxjg[
                                                0][
                                                2]) + '        ' + self.bkg(
                8, self.cxjg[0][3]) + '        ' + self.bkg(8, self.cxjg[0][4]) + '        ' + self.bkg(8,
                                                                                                        self.cxjg[0][
                                                                                                            5]) + '        ' + self.bkg(
                8, self.cxjg[0][6]) + self.bkg(8,
                                               self.cxjg[
                                                   0][
                                                   7]) + self.bkg(8,
                                                                  self.cxjg[
                                                                      0][
                                                                      8]) + self.bkg(8,
                                                                                     self.cxjg[
                                                                                         0][
                                                                                         9]) + self.bkg(8,
                                                                                                        self.cxjg[
                                                                                                            0][
                                                                                                            10]) + '\n\n')
            self.jlxx_text.tag_add('link1', '1.5', '1.7')
            self.jlxx_text.tag_config('link1', foreground='green', underline=True)
            self.jlxx_text.tag_bind('link1', '<Button-1>', self.click1)
        if len(self.cxjg) >= 2:
            self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(8, self.cxjg[1][0]) + self.bkg(8, self.cxjg[1][
                1]) + '        ' + self.bkg(8,
                                            self.cxjg[
                                                1][
                                                2]) + '        ' + self.bkg(
                8, self.cxjg[1][3]) + '        ' + self.bkg(8, self.cxjg[1][4]) + '        ' + self.bkg(8,
                                                                                                        self.cxjg[1][
                                                                                                            5]) + '        ' + self.bkg(
                8, self.cxjg[1][6]) + self.bkg(8,
                                               self.cxjg[
                                                   1][
                                                   7]) + self.bkg(8,
                                                                  self.cxjg[
                                                                      1][
                                                                      8]) + self.bkg(8,
                                                                                     self.cxjg[
                                                                                         1][
                                                                                         9]) + self.bkg(8,
                                                                                                        self.cxjg[
                                                                                                            1][
                                                                                                            10]) + '\n\n')
            self.jlxx_text.tag_add('link2', '3.5', '3.7')
            self.jlxx_text.tag_config('link2', foreground='green', underline=True)
            self.jlxx_text.tag_bind('link2', '<Button-1>', self.click2)
        if len(self.cxjg) >= 3:
            self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(8, self.cxjg[2][0]) + self.bkg(8, self.cxjg[2][
                1]) + '        ' + self.bkg(8,
                                            self.cxjg[
                                                2][
                                                2]) + '        ' + self.bkg(
                8, self.cxjg[2][3]) + '        ' + self.bkg(8, self.cxjg[2][4]) + '        ' + self.bkg(8,
                                                                                                        self.cxjg[2][
                                                                                                            5]) + '        ' + self.bkg(
                8, self.cxjg[2][6]) + self.bkg(8,
                                               self.cxjg[
                                                   2][
                                                   7]) + self.bkg(8,
                                                                  self.cxjg[
                                                                      2][
                                                                      8]) + self.bkg(8,
                                                                                     self.cxjg[
                                                                                         2][
                                                                                         9]) + self.bkg(8,
                                                                                                        self.cxjg[
                                                                                                            2][
                                                                                                            10]) + '\n\n')
            self.jlxx_text.tag_add('link3', '5.5', '5.7')
            self.jlxx_text.tag_config('link3', foreground='green', underline=True)
            self.jlxx_text.tag_bind('link3', '<Button-1>', self.click3)
        if len(self.cxjg) >= 4:
            self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(8, self.cxjg[3][0]) + self.bkg(8, self.cxjg[3][
                1]) + '        ' + self.bkg(8,
                                            self.cxjg[
                                                3][
                                                2]) + '        ' + self.bkg(
                8, self.cxjg[3][3]) + '        ' + self.bkg(8, self.cxjg[3][4]) + '        ' + self.bkg(8,
                                                                                                        self.cxjg[3][
                                                                                                            5]) + '        ' + self.bkg(
                8, self.cxjg[3][6]) + self.bkg(8,
                                               self.cxjg[
                                                   3][
                                                   7]) + self.bkg(8,
                                                                  self.cxjg[
                                                                      3][
                                                                      8]) + self.bkg(8,
                                                                                     self.cxjg[
                                                                                         3][
                                                                                         9]) + self.bkg(8,
                                                                                                        self.cxjg[
                                                                                                            3][
                                                                                                            10]) + '\n\n')
            self.jlxx_text.tag_add('link4', '7.5', '7.7')
            self.jlxx_text.tag_config('link4', foreground='green', underline=True)
            self.jlxx_text.tag_bind('link4', '<Button-1>', self.click4)
        if len(self.cxjg) >= 5:
            self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(8, self.cxjg[4][0]) + self.bkg(8, self.cxjg[4][
                1]) + '        ' + self.bkg(8,
                                            self.cxjg[
                                                4][
                                                2]) + '        ' + self.bkg(
                8, self.cxjg[4][3]) + '        ' + self.bkg(8, self.cxjg[4][4]) + '        ' + self.bkg(8,
                                                                                                        self.cxjg[4][
                                                                                                            5]) + '        ' + self.bkg(
                8, self.cxjg[4][6]) + self.bkg(8,
                                               self.cxjg[
                                                   4][
                                                   7]) + self.bkg(8,
                                                                  self.cxjg[
                                                                      4][
                                                                      8]) + self.bkg(8,
                                                                                     self.cxjg[
                                                                                         4][
                                                                                         9]) + self.bkg(8,
                                                                                                        self.cxjg[
                                                                                                            4][
                                                                                                            10]) + '\n\n')
            self.jlxx_text.tag_add('link5', '9.5', '9.7')
            self.jlxx_text.tag_config('link5', foreground='green', underline=True)
            self.jlxx_text.tag_bind('link5', '<Button-1>', self.click5)
        if len(self.cxjg) >= 6:
            self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(8, self.cxjg[5][0]) + self.bkg(8, self.cxjg[5][
                1]) + '        ' + self.bkg(8,
                                            self.cxjg[
                                                5][
                                                2]) + '        ' + self.bkg(
                8, self.cxjg[5][3]) + '        ' + self.bkg(8, self.cxjg[5][4]) + '        ' + self.bkg(8,
                                                                                                        self.cxjg[5][
                                                                                                            5]) + '        ' + self.bkg(
                8, self.cxjg[5][6]) + self.bkg(8,
                                               self.cxjg[
                                                   5][
                                                   7]) + self.bkg(8,
                                                                  self.cxjg[
                                                                      5][
                                                                      8]) + self.bkg(8,
                                                                                     self.cxjg[
                                                                                         5][
                                                                                         9]) + self.bkg(8,
                                                                                                        self.cxjg[
                                                                                                            5][
                                                                                                            10]) + '\n\n')
            self.jlxx_text.tag_add('link6', '11.5', '11.7')
            self.jlxx_text.tag_config('link6', foreground='green', underline=True)
            self.jlxx_text.tag_bind('link6', '<Button-1>', self.click6)
        if len(self.cxjg) >= 7:
            self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(8, self.cxjg[6][0]) + self.bkg(8, self.cxjg[6][
                1]) + '        ' + self.bkg(8,
                                            self.cxjg[
                                                6][
                                                2]) + '        ' + self.bkg(
                8, self.cxjg[6][3]) + '        ' + self.bkg(8, self.cxjg[6][4]) + '        ' + self.bkg(8,
                                                                                                        self.cxjg[6][
                                                                                                            5]) + '        ' + self.bkg(
                8, self.cxjg[6][6]) + self.bkg(8,
                                               self.cxjg[
                                                   6][
                                                   7]) + self.bkg(8,
                                                                  self.cxjg[
                                                                      6][
                                                                      8]) + self.bkg(8,
                                                                                     self.cxjg[
                                                                                         6][
                                                                                         9]) + self.bkg(8,
                                                                                                        self.cxjg[
                                                                                                            6][
                                                                                                            10]) + '\n\n')
            self.jlxx_text.tag_add('link7', '13.5', '13.7')
            self.jlxx_text.tag_config('link7', foreground='green', underline=True)
            self.jlxx_text.tag_bind('link7', '<Button-1>', self.click7)
        if len(self.cxjg) >= 8:
            self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(8, self.cxjg[7][0]) + self.bkg(8, self.cxjg[7][
                1]) + '        ' + self.bkg(8,
                                            self.cxjg[
                                                7][
                                                2]) + '        ' + self.bkg(
                8, self.cxjg[7][3]) + '        ' + self.bkg(8, self.cxjg[7][4]) + '        ' + self.bkg(8,
                                                                                                        self.cxjg[7][
                                                                                                            5]) + '        ' + self.bkg(
                8, self.cxjg[7][6]) + self.bkg(8,
                                               self.cxjg[
                                                   7][
                                                   7]) + self.bkg(8,
                                                                  self.cxjg[
                                                                      7][
                                                                      8]) + self.bkg(8,
                                                                                     self.cxjg[
                                                                                         7][
                                                                                         9]) + self.bkg(8,
                                                                                                        self.cxjg[
                                                                                                            7][
                                                                                                            10]) + '\n\n')
            self.jlxx_text.tag_add('link8', '15.5', '15.7')
            self.jlxx_text.tag_config('link8', foreground='green', underline=True)
            self.jlxx_text.tag_bind('link8', '<Button-1>', self.click8)
        if len(self.cxjg) >= 9:
            self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(8, self.cxjg[8][0]) + self.bkg(8, self.cxjg[8][
                1]) + '        ' + self.bkg(8,
                                            self.cxjg[
                                                8][
                                                2]) + '        ' + self.bkg(
                8, self.cxjg[8][3]) + '        ' + self.bkg(8, self.cxjg[8][4]) + '        ' + self.bkg(8,
                                                                                                        self.cxjg[8][
                                                                                                            5]) + '        ' + self.bkg(
                8, self.cxjg[8][6]) + self.bkg(8,
                                               self.cxjg[
                                                   8][
                                                   7]) + self.bkg(8,
                                                                  self.cxjg[
                                                                      8][
                                                                      8]) + self.bkg(8,
                                                                                     self.cxjg[
                                                                                         8][
                                                                                         9]) + self.bkg(8,
                                                                                                        self.cxjg[
                                                                                                            8][
                                                                                                            10]) + '\n\n')
            self.jlxx_text.tag_add('link9', '17.5', '17.7')
            self.jlxx_text.tag_config('link9', foreground='green', underline=True)
            self.jlxx_text.tag_bind('link9', '<Button-1>', self.click9)
        if len(self.cxjg) >= 19:
            self.jlxx_text.insert(INSERT, '     详情     ' + self.bkg(8, self.cxjg[9][0]) + self.bkg(8, self.cxjg[9][
                1]) + '        ' + self.bkg(8,
                                            self.cxjg[
                                                9][
                                                2]) + '        ' + self.bkg(
                8, self.cxjg[9][3]) + '        ' + self.bkg(8, self.cxjg[9][4]) + '        ' + self.bkg(8,
                                                                                                        self.cxjg[9][
                                                                                                            5]) + '        ' + self.bkg(
                8, self.cxjg[9][6]) + self.bkg(8,
                                               self.cxjg[
                                                   9][
                                                   7]) + self.bkg(8,
                                                                  self.cxjg[
                                                                      9][
                                                                      8]) + self.bkg(8,
                                                                                     self.cxjg[
                                                                                         9][
                                                                                         9]) + self.bkg(8,
                                                                                                        self.cxjg[
                                                                                                            9][
                                                                                                            10]) + '\n\n')
            self.jlxx_text.tag_add('link10', '19.5', '19.7')
            self.jlxx_text.tag_config('link10', foreground='green', underline=True)
            self.jlxx_text.tag_bind('link10', '<Button-1>', self.click10)
        self.jlxx_text.config(state=DISABLED)


aa = ui()
aa.loding_ui()
