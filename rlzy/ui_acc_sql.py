import pymysql

connect = pymysql.connect(  # 连接数据库服务器
    user="root",
    password="6666",#输入sql的root密码
    host="127.0.0.1",
    port=3306,
    db="mysql",
    charset="utf8"
)
conn = connect.cursor()  # 创建操作游标
conn.execute("use people")  # 选择  课程设计 这个数据库
###############################################################################################################


def check_password(username, password): #检查登录条件
    try:
        user = '''
            select user_password
            from user
            where user_name='%s'
        ''' % username
        conn.execute(user)
        result = conn.fetchall()[0][0]
        if password==result:
            user = '''
                select user_aut
                from user
                where user_name='%s'
            ''' % username
            conn.execute(user)
            result = conn.fetchall()[0][0]
            return result
        else:
            return False
    except:
        return False


def check_zhuche(username, password,ant):#检查注册条件
    if len(username)==0 or len(password)<6:
        return False
    else:
        a=[username, password,ant]
        a='%s' %a
        a=a[1:-1]
        print(a)
        try:
            user = '''
                insert
                into user
                values(%s)
                '''  %a
            conn.execute(user)
            connect.commit()
            user = '''
                 select user_name
                 from user
                 where user_name='%s'
             ''' % username
            conn.execute(user)
            result = conn.fetchall()[0][0]
            if result==username:
                return True
            else:
                return False
        except:
            return False


def acc_sql_i(): #一级下拉框检索
    user='''
        select l_itt_name
        from l_itt
    '''
    conn.execute(user)
    result=conn.fetchall()
    return result

def acc_sql_ii(i_jg): #二级下拉框检索
    user='''
        select ll_itt_name
        from ll_itt
        where ll_bl_l=(
                        select l_itt_no
                        from l_itt
                        where l_itt_name='%s'
                        )
     ''' %i_jg
    conn.execute(user)
    result=conn.fetchall()
    return result

def acc_sql_iii(i_jg): #三级下拉框检索
    user='''
        select lll_itt_name
        from lll_itt
        where lll_bl_ll=(
                        select ll_itt_no
                        from ll_itt
                        where ll_itt_name='%s'
                        )
     ''' %i_jg
    conn.execute(user)
    result=conn.fetchall()
    return result



def cxda_no(l_name,ll_name,lll_name): #获得下一个档案编号字符串
    try:
        user='''
            select lll_itt_no
            from lll_itt
            where lll_itt_name='%s'
         ''' %lll_name
        conn.execute(user)
        result_lll=conn.fetchall()
        user='''
            select ll_itt_no
            from ll_itt
            where ll_itt_name='%s'
         ''' %ll_name
        conn.execute(user)
        result_ll=conn.fetchall()
        user='''
            select l_itt_no
            from l_itt
            where l_itt_name='%s'
         ''' %l_name
        conn.execute(user)
        result_l=conn.fetchall()
        user='''
            select count(*)
            from dangan
            where lll_name='%s'
         ''' %lll_name
        conn.execute(user)
        result_count=conn.fetchall()
        if result_count[0][0]<=9:
            result_count =result_count[0][0]+1
            result_count=str(result_count)
            result_count="0"+result_count
        else:
            result_count = result_count[0][0] + 1
            result_count = str(result_count)
        result="-"+result_l[0][0]+"-"+result_ll[0][0]+"-"+result_lll[0][0]+"-"+result_count
        return result
    except:
        return False


def insert_dangan(list): #档案录入
    a="%s" % list
    a=a[1:-1]
    try:
        user=" insert into dangan(dangan_no,l_name,ll_name,lll_name,zwfl,zwmc,zc,xm,xb,email,dh,qq,sj,zz,yb,gj,csd,sr,mz,zj,zzmm,sfzh,sbhm,nl,xl,jynx,xlzy,xcbz,khh,khzh,djr,djsj,tc,ah,grll,jtgx,bz,dazt) values(%s) " % a
        conn.execute(user)
#        print(user)
        connect.commit()
        return True
    except:
        print("保存错误")
        return False


def danganfuhe(list,aut,zt):#档案复核/修改/删除
    if aut=='人事经理':
        list[-1]=zt
    a="%s" % list
    a=a[1:-1]
    try:
        user="delete from dangan where dangan_no='%s'" %list[0]
        conn.execute(user)
        print(user)
        connect.commit()
        user = " insert into dangan(dangan_no,l_name,ll_name,lll_name,zwfl,zwmc,zc,xm,xb,email,dh,qq,sj,zz,yb,gj,csd,sr,mz,zj,zzmm,sfzh,sbhm,nl,xl,jynx,xlzy,xcbz,khh,khzh,djr,djsj,tc,ah,grll,jtgx,bz,dazt) values(%s) " % a
        conn.execute(user)
        connect.commit()
        return True
    except:
        print("保存错误")
        return False




def dacx_bh(dangan_bh):#档案查询 按编号查找
    user='''
        select *
        from dangan
        where dangan_no='%s'
     '''  % dangan_bh
    conn.execute(user)
    result=conn.fetchall()
    return result

def dacx_xm(dangan_xm):#档案查询 按姓名查找
    user='''
        select *
        from dangan
        where xm='%s'
     '''  % dangan_xm
    conn.execute(user)
    result=conn.fetchall()
    return result

def dacx_xb(dangan_xb):#档案查询 按性别查找
    user='''
        select *
        from dangan
        where xb='%s'
     '''  % dangan_xb
    conn.execute(user)
    result=conn.fetchall()
    return result

def dacx_zw(dangan_zw):#档案查询 按职位查找
    user='''
        select *
        from dangan
        where zwfl='%s'
     '''  % dangan_zw
    conn.execute(user)
    result=conn.fetchall()
    return result





def dacx_jgcx(i_jgcx,ii_jgcx,iii_jgcx,zwfl_jgcx):#档案查询 安条件查找
    string=""
    sand= " and "
    if len(i_jgcx)!=0:
        string="l_name='"+i_jgcx+"'"
    if len(ii_jgcx)!=0 and ii_jgcx!=' ':
        if len(string)==0:
            string = "ll_name='" + ii_jgcx + "'"
        else:
            string=string+sand+"ll_name='"+ii_jgcx+"'"
    if len(iii_jgcx)!=0 and iii_jgcx!=' ':
        if len(string)==0:
            string = "lll_name='" + iii_jgcx + "'"
        else:
            string = string + sand + "lll_name='" + iii_jgcx + "'"
    if len(zwfl_jgcx)!=0:
        if len(string)==0 :
            string = "zwfl='" + zwfl_jgcx + "'"
        else:
            string = string + sand + "zwfl='" + zwfl_jgcx + "'"

    user='''
        select *
        from dangan
        where %s
     '''  % string
    conn.execute(user)
    result=conn.fetchall()
    return result



def dacx_dsh():
    user = '''
            select *
            from dangan
            where dazt='待审核'
         '''
    conn.execute(user)
    result = conn.fetchall()
    return result

def insert_xcxm(list): #薪酬项目录入
    a="%s" % list
    a=a[1:-1]
    print(a)
    try:
        user="insert into xcxm(xcbzbh,xcbzmc,zdr,djsj,zwmc,jbgz,yanglbx,ylbx,sybx,zfgjj,zt) values(%s) " % a
        print(user)
        conn.execute(user)
        connect.commit()
        return True
    except:
        print(user)
        print("保存错误")
        return False

def insert_ygxcdj(list): #薪酬项目录入
    a="%s" % list
    a=a[1:-1]
    print(a)
    try:
        user="insert into ygxc(ygbh,jljj,kcjj,yfze,xcbzbh,djr,zt) values(%s) " % a
        print(user)
        conn.execute(user)
        connect.commit()
        return True
    except:
        print(user)
        print("保存错误")
        return False

def xcbz_dsh():
    user = '''
            select *
            from xcxm
            where zt='fuhe'
         '''
    conn.execute(user)
    result = conn.fetchall()
    return result

def ygxc_sh():
    user = '''
            select *
            from ygxc
            where zt='daifuhe'
         '''
    conn.execute(user)
    result = conn.fetchall()
    return result


# (dangan_no,l_name,ll_name,lll_name,zwfl,zwmc,zc,xm,xb,email,dh,qq,sj,zz,yb,gj,csd,sr,mz,zj,zzmm,sfzh,sbhm,nl,xl,jynx,xlzy,xcbz,khh,khzh,djr,djsj,tc,ah,grll,jtgx,bz,dazt)


# acc_sql2()
# dangan_no="2019-01-01-01-01"
# dacx(dangan_no)
