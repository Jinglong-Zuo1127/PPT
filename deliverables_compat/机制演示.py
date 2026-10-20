from pathlib import Path
import json

def total(items): return sum(v for _, v in items)
def run_travel():
    initial=[('外滩＋南京路',0),('本帮菜午餐',120),('豫园',80),('城隍庙＋游船',220),('地铁',60)]
    observed=[(a,220 if a=='本帮菜午餐' else v) for a,v in initial]
    replanned=[('东北菜午餐',100) if a=='本帮菜午餐' else (a,v) for a,v in observed]
    trace=[{'step':'候选方案','total':total(initial)}, {'step':'教学工具观察：餐费220元','total':total(observed)}, {'step':'检查预算','passes':total(observed)<=500}, {'step':'选择替代午餐','total':total(replanned)}, {'step':'最终费用检查','passes':total(replanned)<=500,'remaining':500-total(replanned)}]
    assert [total(initial),total(observed),total(replanned)]==[480,580,460]
    return trace

def count_only(s): return s.count('(')==s.count(')')
def valid(s):
    balance=0
    for c in s:
        balance += 1 if c=='(' else -1
        if balance<0:return False
    return balance==0

def run_parentheses():
    cases={'':True,'()':True,'(())':True,')(':False,'(()':False,')':False}
    assert count_only(')(') is True and valid(')(') is False
    assert all(valid(s)==answer for s,answer in cases.items())
    return [{'input':s,'expected':v,'count_only':count_only(s),'corrected':valid(s)} for s,v in cases.items()]

if __name__=='__main__':
    result={'scope':'离线教学控制流；固定规则与数据，未调用LLM或真实旅游API','travel':run_travel(),'parentheses':run_parentheses()}
    target=Path(__file__).with_name('机制演示运行记录.json')
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2))
    print(json.dumps(result,ensure_ascii=False,indent=2))
