import tkinter as tk
from enum import Enum
import re
import pandas
import pandastable as pt
from nltk import tree
from classes import *


def Parse():
    pass


'''def Parse():
    j = 0
    Children = []
    Header_dict = Header(j)
    block_dict = block(Header_dict["index"])
    Children.append(Header_dict["node"])  ###############
    Children.append(block_dict["node"])
    dic_output = Match(token_type.Dot, block_dict["index"])

    Children.append(dic_output["node"])
    Node = Tree('Program', Children)

    return Node'''
'''
########################
def Header(j):
    Children = []
    out = dict()
    dic_output_pro = Match(token_type.Program, j)
    dic_output_id = Match(token_type.Identifier, dic_output_pro["index"])
    dic_output_semi = Match(token_type.Semicolon, dic_output_id["index"])
    Children.append(dic_output_pro["node"])
    Children.append(dic_output_id["node"])
    Children.append(dic_output_semi["node"])
    node = Tree('Header', Children)
    out["node"] = node
    out["index"] = dic_output_semi["index"]
    return out


def block(j):
    Children = []
    out = dict()
    dic_output_begin = Match(token_type.Begin, j)
    dic_output_stmt_list = stmt_list(dic_output_begin["index"])
    dic_output_end = Match(token_type.End, dic_output_stmt_list["index"])
    Children.append(dic_output_begin["node"])
    Children.append(dic_output_stmt_list["node"])
    Children.append(dic_output_end["node"])

    node = Tree('block', Children)
    out["node"] = node
    out["index"] = dic_output_end["index"]
    return out


def stmt_list(j):
    Children = []
    out = dict()
    dic_read_write = dict()
    print(Tokens[j].token_type, token_type.Write)
    print("peter peter")

    if (Tokens[j].token_type == token_type.Write):
        dic_read_write = Match(token_type.Write, j)
    elif (Tokens[j].token_type == token_type.Read):
        dic_read_write = Match(token_type.Read, j)
    dic_output_id = Match(token_type.Identifier, dic_read_write["index"])

    Children.append(dic_read_write["node"])
    Children.append(dic_output_id["node"])

    node = Tree('stmt_list', Children)
    out["node"] = node
    out["index"] = dic_output_id["index"]
    return out


def Match(a, j):
    output = dict()
    if (j < len(Tokens)):
        Temp = Tokens[j].to_dict()
        if (Temp['token_type'] == a):
            j += 1
            output["node"] = [Temp['Lex']]
            output["index"] = j
            return output
        else:
            output["node"] = ["error"]
            output["index"] = j + 1
            errors.append("Syntax error : " + Temp['Lex'] + " Expected dot")
            return output
    else:
        output["node"] = ["error"]
        output["index"] = j + 1
        return output
'''