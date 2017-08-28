// -*- Mode: JavaScript; tab-width: 2; indent-tabs-mode: nil; -*-
// vim:set ft=javascript ts=2 sw=2 sts=2 cindent:

var Config = (function(window, undefined) {

    var bratCollData = {
	'entity_types': [
// this is optional
        {
            'type': 'SPAN_DEFAULT',
            'bgColor': '#7fa2ff',
            'borderColor': 'darken'
        },
        {
            'type': 'token',
            'labels': [ '\u00A0\u00A0' ], // non-breaking space for empty
        },
        {
            'type': '-',
            'labels': [ '\u00A0\u00A0' ], // non-breaking space for empty
        }
	],
	'relation_types': [
// this is optional
//         {
//             'type': 'subj',
//             'labels': [ 'subj' ],
//             'dashArray': '3,3',
//             'color': 'green',
//             'args': [
//                 {
//                     'role': 'arg1',
//                     'targets': [ 'token' ]
//                 },
//                 {
//                     'role': 'arg2',
//                     'targets': [ 'token' ]
//                 }
//             ]
//         }
        ],
	'event_types': [],
        'entity_attribute_types': [
// this is optional
        {
            'type': 'Name',
            'values': {
                'Name': { 
                    'glyph': 'Ⓝ',
                    'glyphColor': 'red', 
                    'position': 'right', 
                }
            }
        },
        {
            'type': 'Intentional',
            'values': {
                'Intentional': { 
                    'glyph': 'Ⓘ',
                    'glyphColor': 'red', 
                    'position': 'right', 
                }
            }
        },
        {
            'type': 'Judgment',
            'values': {
                'Judgment': { 
                    'glyph': 'Ⓙ',
                    'glyphColor': 'red', 
                    'position': 'right', 
                }
            }
        }
        ],
    };

    return {
        bratCollData: bratCollData,
    };
})(window);
