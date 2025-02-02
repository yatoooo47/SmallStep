PGDMP      $                 }         
   Small_Step    17.1    17.1 (               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false                       1262    33177 
   Small_Step    DATABASE        CREATE DATABASE "Small_Step" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Japanese_Japan.932';
    DROP DATABASE "Small_Step";
                     postgres    false            �            1259    33178    alembic_version    TABLE     X   CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);
 #   DROP TABLE public.alembic_version;
       public         heap r       postgres    false            �            1259    33184    task    TABLE     �   CREATE TABLE public.task (
    id integer NOT NULL,
    task_level integer NOT NULL,
    task_name character varying(255) NOT NULL,
    task_description text
);
    DROP TABLE public.task;
       public         heap r       postgres    false            �            1259    33183    task_id_seq    SEQUENCE     �   CREATE SEQUENCE public.task_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE public.task_id_seq;
       public               postgres    false    219                       0    0    task_id_seq    SEQUENCE OWNED BY     ;   ALTER SEQUENCE public.task_id_seq OWNED BY public.task.id;
          public               postgres    false    218            �            1259    33193    user    TABLE     �   CREATE TABLE public."user" (
    id integer NOT NULL,
    user_id character varying(255) NOT NULL,
    name character varying(100) NOT NULL,
    password character varying(255) NOT NULL,
    user_kind integer NOT NULL
);
    DROP TABLE public."user";
       public         heap r       postgres    false            �            1259    33192    user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE public.user_id_seq;
       public               postgres    false    221                       0    0    user_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;
          public               postgres    false    220            �            1259    33204    user_tag    TABLE     �   CREATE TABLE public.user_tag (
    id integer NOT NULL,
    executor_id character varying(255) NOT NULL,
    approver_id character varying(255) NOT NULL,
    status character varying(50) NOT NULL
);
    DROP TABLE public.user_tag;
       public         heap r       postgres    false            �            1259    33203    user_tag_id_seq    SEQUENCE     �   CREATE SEQUENCE public.user_tag_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.user_tag_id_seq;
       public               postgres    false    223                        0    0    user_tag_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.user_tag_id_seq OWNED BY public.user_tag.id;
          public               postgres    false    222            �            1259    33223    user_task_progress    TABLE     �   CREATE TABLE public.user_task_progress (
    id integer NOT NULL,
    user_id character varying(255) NOT NULL,
    task_id integer NOT NULL,
    is_completed boolean,
    comment text,
    is_approved boolean
);
 &   DROP TABLE public.user_task_progress;
       public         heap r       postgres    false            �            1259    33222    user_task_progress_id_seq    SEQUENCE     �   CREATE SEQUENCE public.user_task_progress_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.user_task_progress_id_seq;
       public               postgres    false    225            !           0    0    user_task_progress_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.user_task_progress_id_seq OWNED BY public.user_task_progress.id;
          public               postgres    false    224            j           2604    33187    task id    DEFAULT     b   ALTER TABLE ONLY public.task ALTER COLUMN id SET DEFAULT nextval('public.task_id_seq'::regclass);
 6   ALTER TABLE public.task ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    218    219    219            k           2604    33196    user id    DEFAULT     d   ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);
 8   ALTER TABLE public."user" ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    221    220    221            l           2604    33207    user_tag id    DEFAULT     j   ALTER TABLE ONLY public.user_tag ALTER COLUMN id SET DEFAULT nextval('public.user_tag_id_seq'::regclass);
 :   ALTER TABLE public.user_tag ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    222    223    223            m           2604    33226    user_task_progress id    DEFAULT     ~   ALTER TABLE ONLY public.user_task_progress ALTER COLUMN id SET DEFAULT nextval('public.user_task_progress_id_seq'::regclass);
 D   ALTER TABLE public.user_task_progress ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    224    225    225                      0    33178    alembic_version 
   TABLE DATA           6   COPY public.alembic_version (version_num) FROM stdin;
    public               postgres    false    217   �-                 0    33184    task 
   TABLE DATA           K   COPY public.task (id, task_level, task_name, task_description) FROM stdin;
    public               postgres    false    219   �-                 0    33193    user 
   TABLE DATA           H   COPY public."user" (id, user_id, name, password, user_kind) FROM stdin;
    public               postgres    false    221   o<                 0    33204    user_tag 
   TABLE DATA           H   COPY public.user_tag (id, executor_id, approver_id, status) FROM stdin;
    public               postgres    false    223   �=                 0    33223    user_task_progress 
   TABLE DATA           f   COPY public.user_task_progress (id, user_id, task_id, is_completed, comment, is_approved) FROM stdin;
    public               postgres    false    225   �=       "           0    0    task_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.task_id_seq', 90, true);
          public               postgres    false    218            #           0    0    user_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('public.user_id_seq', 2, true);
          public               postgres    false    220            $           0    0    user_tag_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.user_tag_id_seq', 1, true);
          public               postgres    false    222            %           0    0    user_task_progress_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.user_task_progress_id_seq', 90, true);
          public               postgres    false    224            o           2606    33182 #   alembic_version alembic_version_pkc 
   CONSTRAINT     j   ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);
 M   ALTER TABLE ONLY public.alembic_version DROP CONSTRAINT alembic_version_pkc;
       public                 postgres    false    217            q           2606    33191    task task_pkey 
   CONSTRAINT     L   ALTER TABLE ONLY public.task
    ADD CONSTRAINT task_pkey PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.task DROP CONSTRAINT task_pkey;
       public                 postgres    false    219            s           2606    33200    user user_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_pkey;
       public                 postgres    false    221            w           2606    33211    user_tag user_tag_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.user_tag
    ADD CONSTRAINT user_tag_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.user_tag DROP CONSTRAINT user_tag_pkey;
       public                 postgres    false    223            y           2606    33230 *   user_task_progress user_task_progress_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.user_task_progress
    ADD CONSTRAINT user_task_progress_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY public.user_task_progress DROP CONSTRAINT user_task_progress_pkey;
       public                 postgres    false    225            u           2606    33202    user user_user_id_key 
   CONSTRAINT     U   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_user_id_key UNIQUE (user_id);
 A   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_user_id_key;
       public                 postgres    false    221            z           2606    33212 "   user_tag user_tag_approver_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.user_tag
    ADD CONSTRAINT user_tag_approver_id_fkey FOREIGN KEY (approver_id) REFERENCES public."user"(user_id);
 L   ALTER TABLE ONLY public.user_tag DROP CONSTRAINT user_tag_approver_id_fkey;
       public               postgres    false    221    4725    223            {           2606    33217 "   user_tag user_tag_executor_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.user_tag
    ADD CONSTRAINT user_tag_executor_id_fkey FOREIGN KEY (executor_id) REFERENCES public."user"(user_id);
 L   ALTER TABLE ONLY public.user_tag DROP CONSTRAINT user_tag_executor_id_fkey;
       public               postgres    false    221    4725    223            |           2606    33231 2   user_task_progress user_task_progress_task_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.user_task_progress
    ADD CONSTRAINT user_task_progress_task_id_fkey FOREIGN KEY (task_id) REFERENCES public.task(id);
 \   ALTER TABLE ONLY public.user_task_progress DROP CONSTRAINT user_task_progress_task_id_fkey;
       public               postgres    false    219    4721    225            }           2606    33236 2   user_task_progress user_task_progress_user_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.user_task_progress
    ADD CONSTRAINT user_task_progress_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(user_id);
 \   ALTER TABLE ONLY public.user_task_progress DROP CONSTRAINT user_task_progress_user_id_fkey;
       public               postgres    false    225    221    4725                  x�320J�05NJI4L����� *�         g  x��ZKS#�>k~����پ8��>�h����n�@�A#1B�^i� H0�1���>�_pfVUwU�%v�A���zd�_f)�H&��'g��|+�F�o��{8�����Øm��F}f�`�vw�l��'�uc[Ƕuk[�m>�V�6@�mT��!��V�mc�����޷�+WA� Y���uG|�Yk�f�U'��	��4`3�"�V��®��CP��p��mm��Y��%<����ƶ��j�
g�53�T.�M>�[]�>��'��q1��u�h�B4�\R�$�����+���"���4�Z|�N��6����鶁�N������F'�Y*��{�����m���E
��"�P޲�m���2�r� ����TϿ�b���#p�6�8H�������Ҷ���k��Um���r�#���ǳ͎m���9��W4Ҭ��D:�M��V�f������Q�M�ZN�����@8��4��%P�n�l�"p�]˯\G]{v������[���š�?	��V�y��Ml������LG���#�>���o�h���8-�4߇��� %�л���9Y��QF�����g��Ӑ"*P�e��`[hKgc�����Y�O�^ĵ���5�v��N�m���ˀ::8������箘N0�gCY`�rEQLHfaOn����i�Y��b?�n"����� ��1���Bm{�<J�ª�6��$�rq:�	���i����K�j�)�@~���}��
�ѼGK �[p�C ho��,��V6��[��Q,6�D���`.f�/�����A��W@��^C�������M4@�!XT�.�PG�WZŕd��N���D�t��t��0��醊sD��\�<�E�a�kۼ�����-R��%X���(���$��$��������9�����x��E�	7t����0�!ڶi��ϸ��0�r��3zr?BaHso5�R)X�?��'| $�6�d����{�ߐJɓ�y��A�T��ȓt{�:��a(�i�sae�3�Wr�	�ʺ �RB�����i����{�!,os���7_L�'���dY5;��Q�m�ٵ[gm�N޼NY	w��$0�����Ӄ;9�f�T�4���T�o�����K?�MƬ5�b�7:�n&"�N���<����`���nd6d�D�"D�WJ�J�-�Rc��~qw7�c{��Kȭ��+���lo>��HJ���E�{Tgc�`�v��;��G��ɽ�ጁ���v�J��morD9�O��.�FP+�5�E�;zqN
���ׂ�^�y	�Z:}ހHw�����jG8,a]���x�Z'�� B92�y{!]Sր�u�]P�ѭ����+����7v�r���3�� T����J�<� ^���
W���pP��5WH���V�[�T�OO�I�&��4�5�����J$f����}�N�D�Ds�t���	vC, ;A��W�sB�Z��$?.�)�&B2������D.$ �����Iɵ�W�^w����#�QѨ�<��<c�t9�Ap(os�ٿ� ����N������ЅyL�L1�$ >��z�D�m5/�v�KyZ&:U�dw��@D��XA���Z�����7���@�>����H���9!HB(J_'3��J�������EJ�x�"^��Df���(%���� ���
,3�4���δ��Y������0_uIg�O���'�� "4b2D&	k��0ƫ��*�p��b�$��f��H�Gȁ�� T�ЗI�2�8-�#��êxea�2������H��ɚׂ{�q��`&q�Bc�4,Ak����fKVq�a��@�9<��y�u������Z��ɐ�_�G�C�G�K��g��#Tڀ�����!�&�z�p+�k՛�&�lh�a5�A��H�p�}ʪu��+Oj�x�W��9Xש������jH;�.'��h޴��>֭�P��2쉧p��Э�BE��+��"���E�j~�r���nd��nw�5%u�
GD[`s�a�>�����8��*3��n�� JuV�Q�x�N��g�!���p���8��̛�ì��/���\B��
�y���м<�fQ������� t�I�0}�HM�M�V#����R����J_��9���R��5{4bʰl
���o�dC� 4O"0Bp,(5̦��o�(�<�yCwإ���ɫ��tX��h�@����;���>�L�H8D�&Ku����l�E}�J��r�)'�<�������A�nօu­d+	��	g�	B���Y��]�N��H7�6Y����,.���$>W%�Nt+|�p�C��h�	�y�;X�����E�,�{�yRBP��ι��(,)/� 0�M��
��w��	���0Ÿ	���
��"�������� ��IU��h�}��L�X�r���D��+�Zz|�<W|�D
 ���k�Oz�,��m �a�А�r*� =��c�m��?�v�ߜZG-��Lu���,8�gG�\ϻ�:�65� \*4�TKb��(���"��}/�-�m��X2�"z� ���I�l��`����)>��WK��'�T�6���)�����:"�%'��n,��U��@U�Z�?(^~�������r�U�ݱf��B� Ï���&�G�"�����b�U �p�K��Hhnv�ܭ�s���Rc^�f�9\�s%�pn&j.���ơ�/�$��
�#%_x��طn�C�K�:���)��U����Z��"��N��\�ަ[�a>�}܂B����jM0���O���%�%>h���l�����k��@@�!@��U�J!ӣd��-'a@m��f;�P�9����`B��\N+�{ΤFO:��� ͈�GL�~�����Ϗ������#� �����6=����F $]t�n�Ul�7�&�6=h�w���ѡ�@��r�4�C}��}��WE��q +lt͏wX���&��MJ��eI$.E�"-E�S�2d��/�j_#\,˽E�����=�~k��b2`���Y�X:藈i����\x>�������$��"J�jk�}�͞�;�k���p��.������y/F�>c�Q�j�ٌ{!\"���Zegk���Muջ�	�hq¼!��[h�3��*.��2�%���N�.�wl�ϣ
��*YBu�(#]�BJ'�,Bv*���˷2�.��Ө�J�V˞|��+f<9��I��l���u��
~�(�n����~�K�WҸ�|=��&>� !��~zA�.�J���GAAl��Ӯ^HwK'��P۫��;吗 �CJ�Rd���<����d����]»��;�;�R��V{����Ѧl�{��4or���o�jNm-.Rn6�MIV}�ewJcp@A�q_���ֈ4I~O���K���"��"D��Vގ��e���) �����;���UR R��3���7S�X��s���%����B�rl|*��]�[��g	���g�ƨ�l?_p�n�ǂ�B���]b����P/�%�k��;/���9KkL5J�0s�V)7ԁ��i)8��t�e􅱗�ҧ�~�(�Շ��Ç�Q_,|         "  x�m��JCAE�{�#��ǜy��>)A��9s�؈$��K%k�.��~��/{��.��"+����e�}��l���a������)�8�S���lQ�ǳ�I<���لS�#XҾZ���Z����R%���{F��K0���V}S�R��Ր�a
.��u:Ŗ% cr�� TFԮt>(8����ʰ�=|�^��?����_�֌�����&�,ClBN��˘8�Y��W�,W��!�?�%{g�bh��X�	H�\H�i�����D�t�8�Z�\�4�x~0��/�[q�         *   x�3�4H544N6L�4I3IK4M6�L,((�/KM����� ���         �  x�M�;nTAF���b����1�`ΐg�� "�x$�"$$63�]0���d�����ʷ��1��8m�������0W�{��bo�Z�V���j���jǽ����ԡj������D�!� jH5�r��d�!��f�l&��f�l&��f�l&��f�l&��f�l&���9l.���9l.���9l.���9l.���9l.ۄm�6a��Mئl���?�l�)ۄm�6a��Mئl�)[��l![��l![�k�p����l[���l[Ȗ��l	[ʖ��l	[ʖ��l	[���)[�%l)[�l%[�V�l%[�V�l%[�V�l��?ǿl[�V��l[�ְ�l[�ְ�l[�ְ�l[�ְ��m\n�5l-����oX��������;{����O������|=|���׫��^����r�����������-��>;���}     