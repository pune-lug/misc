#!/opt/local/bin/python3.2
# -*- coding: utf-8 -*-


from pprint import pprint

mr_iscii_utf8_map = {
    chr(161): '\u0901',
    chr(162): '\u0902',
    chr(163): '\u0903',
    chr(164): '\u0905',
    chr(165): '\u0906',
    chr(166): '\u0907',
    chr(167): '\u0908',
    chr(168): '\u0909',
    chr(169): '\u090a',
    chr(170): '\u090b',
    chr(171): '\u090e',
    chr(172): '\u090f',
    chr(173): '\u0910',
    chr(174): '\u090d',
    chr(175): '\u0912',
    chr(176): '\u0913',
    chr(177): '\u0914',
    chr(178): '\u0911',
    chr(179): '\u0915',
    chr(180): '\u0916',
    chr(181): '\u0917',
    chr(182): '\u0918',
    chr(183): '\u0919',
    chr(184): '\u091a',
    chr(185): '\u091b',
    chr(186): '\u091c',
    chr(187): '\u091d',
    chr(188): '\u091e',
    chr(189): '\u091f',
    chr(190): '\u0920',
    chr(191): '\u0921',
    chr(192): '\u0922',
    chr(193): '\u0923',
    chr(194): '\u0924',
    chr(195): '\u0925',
    chr(196): '\u0926',
    chr(197): '\u0927',
    chr(198): '\u0928',
    chr(199): '\u0929',
    chr(200): '\u092a',
    chr(201): '\u092b',
    chr(202): '\u092c',
    chr(203): '\u092d',
    chr(204): '\u092e',
    chr(205): '\u092f',
    chr(206): '\u095f',
    chr(207): '\u0930',
    chr(208): '\u0931',
    chr(209): '\u0932',
    chr(210): '\u0933',
    chr(211): '\u0934',
    chr(212): '\u0935',
    chr(213): '\u0936',
    chr(214): '\u0937',
    chr(215): '\u0938',
    chr(216): '\u0939',
    chr(217): '\u25cc',
    chr(218): '\u093e',
    chr(219): '\u093f',
    chr(220): '\u0940',
    chr(221): '\u0941',
    chr(222): '\u0942',
    chr(223): '\u0943',
    chr(224): '\u0946',
    chr(225): '\u0947',
    chr(226): '\u0948',
    chr(227): '\u0945',
    chr(228): '\u094a',
    chr(229): '\u094b',
    chr(230): '\u094c',
    chr(231): '\u0949',
    chr(232): '\u094d',
    chr(233): '\u093c',
    chr(234): '\u0964',
    chr(241): '\u0966',
    chr(242): '\u0967',
    chr(243): '\u0968',
    chr(244): '\u0969',
    chr(245): '\u096a',
    chr(246): '\u096b',
    chr(247): '\u096c',
    chr(248): '\u096d',
    chr(249): '\u096e',
    chr(250): '\u096f',
    '%c%c' % (161, 233): '\u0950',
    '%c%c' % (166, 233): '\u090C',
    '%c%c' % (167, 233): '\u0961',
    '%c%c' % (176, 233): '\u0960',
    '%c%c' % (179, 233): '\u0958',
    '%c%c' % (180, 233): '\u0959',
    '%c%c' % (181, 233): '\u095a',
    '%c%c' % (186, 233): '\u095b',
    '%c%c' % (191, 233): '\u095c',
    '%c%c' % (192, 233): '\u095d',
    '%c%c' % (201, 233): '\u095e',
    '%c%c' % (219, 233): '\u0962',
    '%c%c' % (220, 233): '\u0963',
    '%c%c' % (223, 233): '\u0944',
    '%c%c' % (234, 233): '\u0964',

}


def iscii_utf8(i):
    buf = None
    get_next = [x[0] for x in mr_iscii_utf8_map if len(x) == 2]
    for x in i:
        if x in get_next:
            buf = x
            continue
        if buf:
            if buf+x in mr_iscii_utf8_map:
                yield mr_iscii_utf8_map[buf+x]
            else:
                yield mr_iscii_utf8_map[buf]
                yield mr_iscii_utf8_map[x]
                buf = None
        else:
            if x in mr_iscii_utf8_map:
                yield mr_iscii_utf8_map[x]
            else:
                yield x
    return


def main():
    a = ['%c' % x for x in [65,' ', 165, 201, 209, 219, 233]]
    t = iscii_utf8(a)
    print(t)
    print(''.join([x for x in t]))

if __name__ == '__main__':
    main()
