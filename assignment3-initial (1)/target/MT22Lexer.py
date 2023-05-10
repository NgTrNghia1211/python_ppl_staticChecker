# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01dd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\2\7")
        buf.write("\2\u0086\n\2\f\2\16\2\u0089\13\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\7\3\u0091\n\3\f\3\16\3\u0094\13\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\63\7\63\u0154")
        buf.write("\n\63\f\63\16\63\u0157\13\63\3\64\3\64\3\64\7\64\u015c")
        buf.write("\n\64\f\64\16\64\u015f\13\64\3\64\3\64\6\64\u0163\n\64")
        buf.write("\r\64\16\64\u0164\7\64\u0167\n\64\f\64\16\64\u016a\13")
        buf.write("\64\3\64\3\64\5\64\u016e\n\64\3\65\3\65\3\65\6\65\u0173")
        buf.write("\n\65\r\65\16\65\u0174\3\65\3\65\3\65\3\65\3\65\3\65\6")
        buf.write("\65\u017d\n\65\r\65\16\65\u017e\3\65\3\65\5\65\u0183\n")
        buf.write("\65\3\65\3\65\6\65\u0187\n\65\r\65\16\65\u0188\3\65\3")
        buf.write("\65\3\65\5\65\u018e\n\65\3\66\3\66\7\66\u0192\n\66\f\66")
        buf.write("\16\66\u0195\13\66\3\66\3\66\3\66\3\67\3\67\3\67\5\67")
        buf.write("\u019d\n\67\38\38\38\38\38\38\38\38\38\58\u01a8\n8\39")
        buf.write("\39\3:\3:\3;\3;\3<\3<\5<\u01b2\n<\3<\6<\u01b5\n<\r<\16")
        buf.write("<\u01b6\3=\6=\u01ba\n=\r=\16=\u01bb\3=\3=\3>\3>\7>\u01c2")
        buf.write("\n>\f>\16>\u01c5\13>\3>\3>\5>\u01c9\n>\3>\3>\3?\3?\7?")
        buf.write("\u01cf\n?\f?\16?\u01d2\13?\3?\3?\3?\5?\u01d7\n?\3?\3?")
        buf.write("\3@\3@\3@\3\u0092\2A\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64")
        buf.write("g\65i\66k\67m\2o\2q\2s\2u\2w\2y8{9}:\177;\3\2\17\4\2\f")
        buf.write("\f\17\17\n\2$$))^^ddhhppttvv\6\2\f\f\17\17$$^^\3\2\62")
        buf.write(";\3\2\63;\5\2C\\aac|\4\2GGgg\4\2--//\5\2\13\f\16\17\"")
        buf.write("\"\6\2\f\f\17\17GHQQ\3\2$$\t\2$$^^ddhhppttvv\3\2^^\2\u01ee")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}")
        buf.write("\3\2\2\2\2\177\3\2\2\2\3\u0081\3\2\2\2\5\u008c\3\2\2\2")
        buf.write("\7\u009a\3\2\2\2\t\u009f\3\2\2\2\13\u00a5\3\2\2\2\r\u00ad")
        buf.write("\3\2\2\2\17\u00b0\3\2\2\2\21\u00b5\3\2\2\2\23\u00bb\3")
        buf.write("\2\2\2\25\u00c1\3\2\2\2\27\u00c5\3\2\2\2\31\u00ce\3\2")
        buf.write("\2\2\33\u00d1\3\2\2\2\35\u00d9\3\2\2\2\37\u00e0\3\2\2")
        buf.write("\2!\u00e7\3\2\2\2#\u00ec\3\2\2\2%\u00f2\3\2\2\2\'\u00f7")
        buf.write("\3\2\2\2)\u00fb\3\2\2\2+\u0104\3\2\2\2-\u0107\3\2\2\2")
        buf.write("/\u010f\3\2\2\2\61\u0115\3\2\2\2\63\u0117\3\2\2\2\65\u0119")
        buf.write("\3\2\2\2\67\u011b\3\2\2\29\u011d\3\2\2\2;\u011f\3\2\2")
        buf.write("\2=\u0121\3\2\2\2?\u0124\3\2\2\2A\u0127\3\2\2\2C\u012a")
        buf.write("\3\2\2\2E\u012d\3\2\2\2G\u012f\3\2\2\2I\u0131\3\2\2\2")
        buf.write("K\u0134\3\2\2\2M\u0137\3\2\2\2O\u013a\3\2\2\2Q\u013c\3")
        buf.write("\2\2\2S\u013e\3\2\2\2U\u0140\3\2\2\2W\u0142\3\2\2\2Y\u0144")
        buf.write("\3\2\2\2[\u0146\3\2\2\2]\u0148\3\2\2\2_\u014a\3\2\2\2")
        buf.write("a\u014c\3\2\2\2c\u014e\3\2\2\2e\u0150\3\2\2\2g\u016d\3")
        buf.write("\2\2\2i\u018d\3\2\2\2k\u018f\3\2\2\2m\u019c\3\2\2\2o\u01a7")
        buf.write("\3\2\2\2q\u01a9\3\2\2\2s\u01ab\3\2\2\2u\u01ad\3\2\2\2")
        buf.write("w\u01af\3\2\2\2y\u01b9\3\2\2\2{\u01bf\3\2\2\2}\u01cc\3")
        buf.write("\2\2\2\177\u01da\3\2\2\2\u0081\u0082\7\61\2\2\u0082\u0083")
        buf.write("\7\61\2\2\u0083\u0087\3\2\2\2\u0084\u0086\n\2\2\2\u0085")
        buf.write("\u0084\3\2\2\2\u0086\u0089\3\2\2\2\u0087\u0085\3\2\2\2")
        buf.write("\u0087\u0088\3\2\2\2\u0088\u008a\3\2\2\2\u0089\u0087\3")
        buf.write("\2\2\2\u008a\u008b\b\2\2\2\u008b\4\3\2\2\2\u008c\u008d")
        buf.write("\7\61\2\2\u008d\u008e\7,\2\2\u008e\u0092\3\2\2\2\u008f")
        buf.write("\u0091\13\2\2\2\u0090\u008f\3\2\2\2\u0091\u0094\3\2\2")
        buf.write("\2\u0092\u0093\3\2\2\2\u0092\u0090\3\2\2\2\u0093\u0095")
        buf.write("\3\2\2\2\u0094\u0092\3\2\2\2\u0095\u0096\7,\2\2\u0096")
        buf.write("\u0097\7\61\2\2\u0097\u0098\3\2\2\2\u0098\u0099\b\3\2")
        buf.write("\2\u0099\6\3\2\2\2\u009a\u009b\7c\2\2\u009b\u009c\7w\2")
        buf.write("\2\u009c\u009d\7v\2\2\u009d\u009e\7q\2\2\u009e\b\3\2\2")
        buf.write("\2\u009f\u00a0\7d\2\2\u00a0\u00a1\7t\2\2\u00a1\u00a2\7")
        buf.write("g\2\2\u00a2\u00a3\7c\2\2\u00a3\u00a4\7m\2\2\u00a4\n\3")
        buf.write("\2\2\2\u00a5\u00a6\7d\2\2\u00a6\u00a7\7q\2\2\u00a7\u00a8")
        buf.write("\7q\2\2\u00a8\u00a9\7n\2\2\u00a9\u00aa\7g\2\2\u00aa\u00ab")
        buf.write("\7c\2\2\u00ab\u00ac\7p\2\2\u00ac\f\3\2\2\2\u00ad\u00ae")
        buf.write("\7f\2\2\u00ae\u00af\7q\2\2\u00af\16\3\2\2\2\u00b0\u00b1")
        buf.write("\7g\2\2\u00b1\u00b2\7n\2\2\u00b2\u00b3\7u\2\2\u00b3\u00b4")
        buf.write("\7g\2\2\u00b4\20\3\2\2\2\u00b5\u00b6\7h\2\2\u00b6\u00b7")
        buf.write("\7c\2\2\u00b7\u00b8\7n\2\2\u00b8\u00b9\7u\2\2\u00b9\u00ba")
        buf.write("\7g\2\2\u00ba\22\3\2\2\2\u00bb\u00bc\7h\2\2\u00bc\u00bd")
        buf.write("\7n\2\2\u00bd\u00be\7q\2\2\u00be\u00bf\7c\2\2\u00bf\u00c0")
        buf.write("\7v\2\2\u00c0\24\3\2\2\2\u00c1\u00c2\7h\2\2\u00c2\u00c3")
        buf.write("\7q\2\2\u00c3\u00c4\7t\2\2\u00c4\26\3\2\2\2\u00c5\u00c6")
        buf.write("\7h\2\2\u00c6\u00c7\7w\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9")
        buf.write("\7e\2\2\u00c9\u00ca\7v\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc")
        buf.write("\7q\2\2\u00cc\u00cd\7p\2\2\u00cd\30\3\2\2\2\u00ce\u00cf")
        buf.write("\7k\2\2\u00cf\u00d0\7h\2\2\u00d0\32\3\2\2\2\u00d1\u00d2")
        buf.write("\7k\2\2\u00d2\u00d3\7p\2\2\u00d3\u00d4\7v\2\2\u00d4\u00d5")
        buf.write("\7g\2\2\u00d5\u00d6\7i\2\2\u00d6\u00d7\7g\2\2\u00d7\u00d8")
        buf.write("\7t\2\2\u00d8\34\3\2\2\2\u00d9\u00da\7t\2\2\u00da\u00db")
        buf.write("\7g\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd\7w\2\2\u00dd\u00de")
        buf.write("\7t\2\2\u00de\u00df\7p\2\2\u00df\36\3\2\2\2\u00e0\u00e1")
        buf.write("\7u\2\2\u00e1\u00e2\7v\2\2\u00e2\u00e3\7t\2\2\u00e3\u00e4")
        buf.write("\7k\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6\7i\2\2\u00e6 \3")
        buf.write("\2\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9\7t\2\2\u00e9\u00ea")
        buf.write("\7w\2\2\u00ea\u00eb\7g\2\2\u00eb\"\3\2\2\2\u00ec\u00ed")
        buf.write("\7y\2\2\u00ed\u00ee\7j\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0")
        buf.write("\7n\2\2\u00f0\u00f1\7g\2\2\u00f1$\3\2\2\2\u00f2\u00f3")
        buf.write("\7x\2\2\u00f3\u00f4\7q\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6")
        buf.write("\7f\2\2\u00f6&\3\2\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9")
        buf.write("\7w\2\2\u00f9\u00fa\7v\2\2\u00fa(\3\2\2\2\u00fb\u00fc")
        buf.write("\7e\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe\7p\2\2\u00fe\u00ff")
        buf.write("\7v\2\2\u00ff\u0100\7k\2\2\u0100\u0101\7p\2\2\u0101\u0102")
        buf.write("\7w\2\2\u0102\u0103\7g\2\2\u0103*\3\2\2\2\u0104\u0105")
        buf.write("\7q\2\2\u0105\u0106\7h\2\2\u0106,\3\2\2\2\u0107\u0108")
        buf.write("\7k\2\2\u0108\u0109\7p\2\2\u0109\u010a\7j\2\2\u010a\u010b")
        buf.write("\7g\2\2\u010b\u010c\7t\2\2\u010c\u010d\7k\2\2\u010d\u010e")
        buf.write("\7v\2\2\u010e.\3\2\2\2\u010f\u0110\7c\2\2\u0110\u0111")
        buf.write("\7t\2\2\u0111\u0112\7t\2\2\u0112\u0113\7c\2\2\u0113\u0114")
        buf.write("\7{\2\2\u0114\60\3\2\2\2\u0115\u0116\7-\2\2\u0116\62\3")
        buf.write("\2\2\2\u0117\u0118\7/\2\2\u0118\64\3\2\2\2\u0119\u011a")
        buf.write("\7,\2\2\u011a\66\3\2\2\2\u011b\u011c\7\61\2\2\u011c8\3")
        buf.write("\2\2\2\u011d\u011e\7\'\2\2\u011e:\3\2\2\2\u011f\u0120")
        buf.write("\7#\2\2\u0120<\3\2\2\2\u0121\u0122\7(\2\2\u0122\u0123")
        buf.write("\7(\2\2\u0123>\3\2\2\2\u0124\u0125\7~\2\2\u0125\u0126")
        buf.write("\7~\2\2\u0126@\3\2\2\2\u0127\u0128\7?\2\2\u0128\u0129")
        buf.write("\7?\2\2\u0129B\3\2\2\2\u012a\u012b\7#\2\2\u012b\u012c")
        buf.write("\7?\2\2\u012cD\3\2\2\2\u012d\u012e\7>\2\2\u012eF\3\2\2")
        buf.write("\2\u012f\u0130\7@\2\2\u0130H\3\2\2\2\u0131\u0132\7>\2")
        buf.write("\2\u0132\u0133\7?\2\2\u0133J\3\2\2\2\u0134\u0135\7@\2")
        buf.write("\2\u0135\u0136\7?\2\2\u0136L\3\2\2\2\u0137\u0138\7<\2")
        buf.write("\2\u0138\u0139\7<\2\2\u0139N\3\2\2\2\u013a\u013b\7]\2")
        buf.write("\2\u013bP\3\2\2\2\u013c\u013d\7_\2\2\u013dR\3\2\2\2\u013e")
        buf.write("\u013f\7}\2\2\u013fT\3\2\2\2\u0140\u0141\7\177\2\2\u0141")
        buf.write("V\3\2\2\2\u0142\u0143\7*\2\2\u0143X\3\2\2\2\u0144\u0145")
        buf.write("\7+\2\2\u0145Z\3\2\2\2\u0146\u0147\7\60\2\2\u0147\\\3")
        buf.write("\2\2\2\u0148\u0149\7.\2\2\u0149^\3\2\2\2\u014a\u014b\7")
        buf.write("=\2\2\u014b`\3\2\2\2\u014c\u014d\7<\2\2\u014db\3\2\2\2")
        buf.write("\u014e\u014f\7?\2\2\u014fd\3\2\2\2\u0150\u0155\5u;\2\u0151")
        buf.write("\u0154\5u;\2\u0152\u0154\5q9\2\u0153\u0151\3\2\2\2\u0153")
        buf.write("\u0152\3\2\2\2\u0154\u0157\3\2\2\2\u0155\u0153\3\2\2\2")
        buf.write("\u0155\u0156\3\2\2\2\u0156f\3\2\2\2\u0157\u0155\3\2\2")
        buf.write("\2\u0158\u016e\7\62\2\2\u0159\u015d\5s:\2\u015a\u015c")
        buf.write("\5q9\2\u015b\u015a\3\2\2\2\u015c\u015f\3\2\2\2\u015d\u015b")
        buf.write("\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u0168\3\2\2\2\u015f")
        buf.write("\u015d\3\2\2\2\u0160\u0162\7a\2\2\u0161\u0163\5q9\2\u0162")
        buf.write("\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0162\3\2\2\2")
        buf.write("\u0164\u0165\3\2\2\2\u0165\u0167\3\2\2\2\u0166\u0160\3")
        buf.write("\2\2\2\u0167\u016a\3\2\2\2\u0168\u0166\3\2\2\2\u0168\u0169")
        buf.write("\3\2\2\2\u0169\u016b\3\2\2\2\u016a\u0168\3\2\2\2\u016b")
        buf.write("\u016c\b\64\3\2\u016c\u016e\3\2\2\2\u016d\u0158\3\2\2")
        buf.write("\2\u016d\u0159\3\2\2\2\u016eh\3\2\2\2\u016f\u0170\5g\64")
        buf.write("\2\u0170\u0172\5[.\2\u0171\u0173\5q9\2\u0172\u0171\3\2")
        buf.write("\2\2\u0173\u0174\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175")
        buf.write("\3\2\2\2\u0175\u0183\3\2\2\2\u0176\u0177\5g\64\2\u0177")
        buf.write("\u0178\5w<\2\u0178\u0183\3\2\2\2\u0179\u017a\5g\64\2\u017a")
        buf.write("\u017c\5[.\2\u017b\u017d\5q9\2\u017c\u017b\3\2\2\2\u017d")
        buf.write("\u017e\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2")
        buf.write("\u017f\u0180\3\2\2\2\u0180\u0181\5w<\2\u0181\u0183\3\2")
        buf.write("\2\2\u0182\u016f\3\2\2\2\u0182\u0176\3\2\2\2\u0182\u0179")
        buf.write("\3\2\2\2\u0183\u018e\3\2\2\2\u0184\u0186\5[.\2\u0185\u0187")
        buf.write("\5q9\2\u0186\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0186")
        buf.write("\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018a\3\2\2\2\u018a")
        buf.write("\u018b\5w<\2\u018b\u018c\b\65\4\2\u018c\u018e\3\2\2\2")
        buf.write("\u018d\u0182\3\2\2\2\u018d\u0184\3\2\2\2\u018ej\3\2\2")
        buf.write("\2\u018f\u0193\7$\2\2\u0190\u0192\5m\67\2\u0191\u0190")
        buf.write("\3\2\2\2\u0192\u0195\3\2\2\2\u0193\u0191\3\2\2\2\u0193")
        buf.write("\u0194\3\2\2\2\u0194\u0196\3\2\2\2\u0195\u0193\3\2\2\2")
        buf.write("\u0196\u0197\7$\2\2\u0197\u0198\b\66\5\2\u0198l\3\2\2")
        buf.write("\2\u0199\u019a\7^\2\2\u019a\u019d\t\3\2\2\u019b\u019d")
        buf.write("\n\4\2\2\u019c\u0199\3\2\2\2\u019c\u019b\3\2\2\2\u019d")
        buf.write("n\3\2\2\2\u019e\u019f\7v\2\2\u019f\u01a0\7t\2\2\u01a0")
        buf.write("\u01a1\7w\2\2\u01a1\u01a8\7g\2\2\u01a2\u01a3\7h\2\2\u01a3")
        buf.write("\u01a4\7c\2\2\u01a4\u01a5\7n\2\2\u01a5\u01a6\7u\2\2\u01a6")
        buf.write("\u01a8\7g\2\2\u01a7\u019e\3\2\2\2\u01a7\u01a2\3\2\2\2")
        buf.write("\u01a8p\3\2\2\2\u01a9\u01aa\t\5\2\2\u01aar\3\2\2\2\u01ab")
        buf.write("\u01ac\t\6\2\2\u01act\3\2\2\2\u01ad\u01ae\t\7\2\2\u01ae")
        buf.write("v\3\2\2\2\u01af\u01b1\t\b\2\2\u01b0\u01b2\t\t\2\2\u01b1")
        buf.write("\u01b0\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b4\3\2\2\2")
        buf.write("\u01b3\u01b5\5q9\2\u01b4\u01b3\3\2\2\2\u01b5\u01b6\3\2")
        buf.write("\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7x\3")
        buf.write("\2\2\2\u01b8\u01ba\t\n\2\2\u01b9\u01b8\3\2\2\2\u01ba\u01bb")
        buf.write("\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc")
        buf.write("\u01bd\3\2\2\2\u01bd\u01be\b=\2\2\u01bez\3\2\2\2\u01bf")
        buf.write("\u01c3\7$\2\2\u01c0\u01c2\5m\67\2\u01c1\u01c0\3\2\2\2")
        buf.write("\u01c2\u01c5\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3\u01c4\3")
        buf.write("\2\2\2\u01c4\u01c8\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c6\u01c9")
        buf.write("\t\13\2\2\u01c7\u01c9\n\f\2\2\u01c8\u01c6\3\2\2\2\u01c8")
        buf.write("\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cb\b>\6\2")
        buf.write("\u01cb|\3\2\2\2\u01cc\u01d0\7$\2\2\u01cd\u01cf\5m\67\2")
        buf.write("\u01ce\u01cd\3\2\2\2\u01cf\u01d2\3\2\2\2\u01d0\u01ce\3")
        buf.write("\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d6\3\2\2\2\u01d2\u01d0")
        buf.write("\3\2\2\2\u01d3\u01d4\7^\2\2\u01d4\u01d7\n\r\2\2\u01d5")
        buf.write("\u01d7\n\16\2\2\u01d6\u01d3\3\2\2\2\u01d6\u01d5\3\2\2")
        buf.write("\2\u01d7\u01d8\3\2\2\2\u01d8\u01d9\b?\7\2\u01d9~\3\2\2")
        buf.write("\2\u01da\u01db\13\2\2\2\u01db\u01dc\b@\b\2\u01dc\u0080")
        buf.write("\3\2\2\2\32\2\u0087\u0092\u0153\u0155\u015d\u0164\u0168")
        buf.write("\u016d\u0174\u017e\u0182\u0188\u018d\u0193\u019c\u01a7")
        buf.write("\u01b1\u01b6\u01bb\u01c3\u01c8\u01d0\u01d6\t\b\2\2\3\64")
        buf.write("\2\3\65\3\3\66\4\3>\5\3?\6\3@\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LINE_COMMENT = 1
    BLOCK_COMMENT = 2
    AUTO = 3
    BREAK = 4
    BOOLEAN = 5
    DO = 6
    ELSE = 7
    FALSE = 8
    FLOAT = 9
    FOR = 10
    FUNCTION = 11
    IF = 12
    INTEGER = 13
    RETURN = 14
    STRING = 15
    TRUE = 16
    WHILE = 17
    VOID = 18
    OUT = 19
    CONTINUE = 20
    OF = 21
    INHERIT = 22
    ARRAY = 23
    ADDOP = 24
    SUBOP = 25
    MULOP = 26
    DIVOP = 27
    MODOP = 28
    NOTOP = 29
    ANDOP = 30
    OROP = 31
    EQOP = 32
    DIFOP = 33
    LT = 34
    GT = 35
    LE = 36
    GE = 37
    BELONG = 38
    LSB = 39
    RSB = 40
    LP = 41
    RP = 42
    LB = 43
    RB = 44
    DOT = 45
    COMMA = 46
    SEMI = 47
    COLON = 48
    EQUAL = 49
    IDENTIFIER = 50
    INTLIT = 51
    FLOATLIT = 52
    STRINGLIT = 53
    WS = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56
    ERROR_CHAR = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", 
            "'<='", "'>='", "'::'", "'['", "']'", "'{'", "'}'", "'('", "')'", 
            "'.'", "','", "';'", "':'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "LINE_COMMENT", "BLOCK_COMMENT", "AUTO", "BREAK", "BOOLEAN", 
            "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
            "RETURN", "STRING", "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", 
            "OF", "INHERIT", "ARRAY", "ADDOP", "SUBOP", "MULOP", "DIVOP", 
            "MODOP", "NOTOP", "ANDOP", "OROP", "EQOP", "DIFOP", "LT", "GT", 
            "LE", "GE", "BELONG", "LSB", "RSB", "LP", "RP", "LB", "RB", 
            "DOT", "COMMA", "SEMI", "COLON", "EQUAL", "IDENTIFIER", "INTLIT", 
            "FLOATLIT", "STRINGLIT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "LINE_COMMENT", "BLOCK_COMMENT", "AUTO", "BREAK", "BOOLEAN", 
                  "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", 
                  "INTEGER", "RETURN", "STRING", "TRUE", "WHILE", "VOID", 
                  "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "ADDOP", 
                  "SUBOP", "MULOP", "DIVOP", "MODOP", "NOTOP", "ANDOP", 
                  "OROP", "EQOP", "DIFOP", "LT", "GT", "LE", "GE", "BELONG", 
                  "LSB", "RSB", "LP", "RP", "LB", "RB", "DOT", "COMMA", 
                  "SEMI", "COLON", "EQUAL", "IDENTIFIER", "INTLIT", "FLOATLIT", 
                  "STRINGLIT", "CHAR", "BOOL", "DIGIT", "NONZERO", "NONDIGIT", 
                  "EXPONENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[50] = self.INTLIT_action 
            actions[51] = self.FLOATLIT_action 
            actions[52] = self.STRINGLIT_action 
            actions[60] = self.UNCLOSE_STRING_action 
            actions[61] = self.ILLEGAL_ESCAPE_action 
            actions[62] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_", "")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    self.text = self.text[1:-1]
                
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	err_char = ['\r','\n',EOFError]
            	if self.text[-1] in err_char:
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	raise IllegalEscape(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


