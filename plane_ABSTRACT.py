# -*- coding: cp936 -*-
class Plane(pygame.sprite.Sprite):
    def __init__(self,VELOCITY=100):
        self.velocity = VELOCITY  # �㶨��
        self.accelerate = [0,0]  # û�м��ٶ�ָ���б��ʱ�򣬼��ٶ�Ĭ��Ϊ0
        pass

    def update(self, trace):
        self.accelerate = self.pop_first()
        self.velocity += self.accelerate
        self.position += self.velocity
        self.rect.center = self.position

    def draw(self):
        pass

    def pop_first():
        """ȡ���ٶ��б��һ��ֵ������б�Ϊ�գ�����ٶ�Ϊ��0,0��
        """
        pass

    def plane_form_trace(self):
        end_point = get_mouse_pos()
        start_point = self.position

class Curve(self):
    pass
        
class Player():
    def __init__(self):
        plane_lst = Plane()

    def operation():
        state = State('select,select_ok,set_plane,None')
        if state = 'select':
            res = select_plane()  # [select_ok, select_plane_obj]
            selcet_ok = res[0]
            if select_ok:
                select_plane = res[1]
                state.next()
        elif state = 'set_plane':
            res = select_plane.planeform_trace()  # [set_plane_ok, plane_parameters_lst]
            set_ok = res[0]
            if set_ok:
            select_plane.accelerate_lst = res[1]
            state.next()

class State():
    def __init__(self):
        pass

    def __str__(self):
        pass
    
    def next(self):
        """ȡ��һ��ֵ������б�Ϊ�գ���ȡNone
        """
        pass
main():
    init()
    while(runing):
        if senario = 'Player1':
            player1.operation()
        elif:
            senario = 'Player2':
            player2.operation()
        else:
            runing(steps = 20)

        update_all()
    
