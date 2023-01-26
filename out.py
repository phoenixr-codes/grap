ParsedRule(
    name='main',
    rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586aa10>,
    match='1 + 1',
    span=(0, 5),
    parent=None,
    inner=[
        ParsedRule(
            name='number',
            rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586a860>,
            match='1',
            span=(0, 1),
            parent=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586a860>,
            inner=[
                ParsedRule(
                    name='<function rule at 0x7fda05a3f0a0>+',
                    rule=OnceOrMore(
                        rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586a8c0>,
                        name='<function rule at 0x7fda05a3f0a0>+'
                    ),
                    match='1',
                    span=(0, 1),
                    parent=OnceOrMore(
                        rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586a8c0>,
                        name='<function rule at 0x7fda05a3f0a0>+'
                    ),
                    inner=[
                        ParsedRule(
                            name='digit',
                            rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586a8c0>,
                            match='1',
                            span=(0, 1),
                            parent=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586a8c0>,
                            inner=[
                                ParsedRule(
                                    name="'0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9'",
                                    rule=<grap.core.rules.RuleUnion object at 0x7fda0586ad40>,
                                    match='1',
                                    span=(0, 1),
                                    parent=<grap.core.rules.RuleUnion object at 0x7fda0586ad40>,
                                    inner=[
                                        ParsedRule(
                                            name="'1'",
                                            rule=<grap.core.rules.String object at 0x7fda0586a9b0>,
                                            match='1',
                                            span=(0, 1),
                                            parent=<grap.core.rules.String object at 0x7fda0586a9b0>,
                                            inner=[]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        ),
        ParsedRule(
            name='{self.rule}?',
            rule=Optional(
                rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586b040>,
                name='{self.rule}?'
            ),
            match=' ',
            span=(1, 2),
            parent=Optional(
                rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586b040>,
                name='{self.rule}?'
            ),
            inner=[
                ParsedRule(
                    name='whitespace',
                    rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586b040>,
                    match=' ',
                    span=(1, 2),
                    parent=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586b040>,
                    inner=[
                        ParsedRule(
                            name='<function rule at 0x7fda05a3f0a0>+',
                            rule=OnceOrMore(rule=' ', name='<function rule at 0x7fda05a3f0a0>+'),
                            match=' ',
                            span=(1, 2),
                            parent=OnceOrMore(rule=' ', name='<function rule at 0x7fda05a3f0a0>+'),
                            inner=[]
                        )
                    ]
                )
            ]
        ),
        ParsedRule(
            name='operator',
            rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586ada0>,
            match='+',
            span=(2, 3),
            parent=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586ada0>,
            inner=[
                ParsedRule(
                    name="'+'|'-'|'*'|'/'",
                    rule=<grap.core.rules.RuleUnion object at 0x7fda0586a5f0>,
                    match='+',
                    span=(2, 3),
                    parent=<grap.core.rules.RuleUnion object at 0x7fda0586a5f0>,
                    inner=[
                        ParsedRule(
                            name="'+'",
                            rule=<grap.core.rules.String object at 0x7fda0586a890>,
                            match='+',
                            span=(2, 3),
                            parent=<grap.core.rules.String object at 0x7fda0586a890>,
                            inner=[]
                        )
                    ]
                )
            ]
        ),
        ParsedRule(
            name='{self.rule}?',
            rule=Optional(
                rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586aec0>,
                name='{self.rule}?'
            ),
            match=' ',
            span=(3, 4),
            parent=Optional(
                rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586aec0>,
                name='{self.rule}?'
            ),
            inner=[
                ParsedRule(
                    name='whitespace',
                    rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586aec0>,
                    match=' ',
                    span=(3, 4),
                    parent=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586aec0>,
                    inner=[
                        ParsedRule(
                            name='<function rule at 0x7fda05a3f0a0>+',
                            rule=OnceOrMore(rule=' ', name='<function rule at 0x7fda05a3f0a0>+'),
                            match=' ',
                            span=(3, 4),
                            parent=OnceOrMore(rule=' ', name='<function rule at 0x7fda05a3f0a0>+'),
                            inner=[]
                        )
                    ]
                )
            ]
        ),
        ParsedRule(
            name='number',
            rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586af80>,
            match='1',
            span=(4, 5),
            parent=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586af80>,
            inner=[
                ParsedRule(
                    name='<function rule at 0x7fda05a3f0a0>+',
                    rule=OnceOrMore(
                        rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586b190>,
                        name='<function rule at 0x7fda05a3f0a0>+'
                    ),
                    match='1',
                    span=(4, 5),
                    parent=OnceOrMore(
                        rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586b190>,
                        name='<function rule at 0x7fda05a3f0a0>+'
                    ),
                    inner=[
                        ParsedRule(
                            name='digit',
                            rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586b190>,
                            match='1',
                            span=(4, 5),
                            parent=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586b190>,
                            inner=[
                                ParsedRule(
                                    name="'0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9'",
                                    rule=<grap.core.rules.RuleUnion object at 0x7fda0586b400>,
                                    match='1',
                                    span=(4, 5),
                                    parent=<grap.core.rules.RuleUnion object at 0x7fda0586b400>,
                                    inner=[
                                        ParsedRule(
                                            name="'1'",
                                            rule=<grap.core.rules.String object at 0x7fda0586aef0>,
                                            match='1',
                                            span=(4, 5),
                                            parent=<grap.core.rules.String object at 0x7fda0586aef0>,
                                            inner=[]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)
ParsedRule(
    name='main',
    rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda05623c70>,
    match='69  *420',
    span=(0, 8),
    parent=None,
    inner=[
        ParsedRule(
            name='number',
            rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda055e7760>,
            match='69',
            span=(0, 2),
            parent=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda055e7760>,
            inner=[
                ParsedRule(
                    name='<function rule at 0x7fda05a3f0a0>+',
                    rule=OnceOrMore(
                        rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda055e7610>,
                        name='<function rule at 0x7fda05a3f0a0>+'
                    ),
                    match='69',
                    span=(0, 2),
                    parent=OnceOrMore(
                        rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda055e7610>,
                        name='<function rule at 0x7fda05a3f0a0>+'
                    ),
                    inner=[
                        ParsedRule(
                            name='digit',
                            rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda055e7610>,
                            match='6',
                            span=(0, 1),
                            parent=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda055e7610>,
                            inner=[
                                ParsedRule(
                                    name="'0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9'",
                                    rule=<grap.core.rules.RuleUnion object at 0x7fda0586ab00>,
                                    match='6',
                                    span=(0, 1),
                                    parent=<grap.core.rules.RuleUnion object at 0x7fda0586ab00>,
                                    inner=[
                                        ParsedRule(
                                            name="'6'",
                                            rule=<grap.core.rules.String object at 0x7fda0586ad70>,
                                            match='6',
                                            span=(0, 1),
                                            parent=<grap.core.rules.String object at 0x7fda0586ad70>,
                                            inner=[]
                                        )
                                    ]
                                )
                            ]
                        ),
                        ParsedRule(
                            name='digit',
                            rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda055e7610>,
                            match='9',
                            span=(1, 2),
                            parent=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda055e7610>,
                            inner=[
                                ParsedRule(
                                    name="'0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9'",
                                    rule=<grap.core.rules.RuleUnion object at 0x7fda0586ae60>,
                                    match='9',
                                    span=(1, 2),
                                    parent=<grap.core.rules.RuleUnion object at 0x7fda0586ae60>,
                                    inner=[
                                        ParsedRule(
                                            name="'9'",
                                            rule=<grap.core.rules.String object at 0x7fda0586a6b0>,
                                            match='9',
                                            span=(1, 2),
                                            parent=<grap.core.rules.String object at 0x7fda0586a6b0>,
                                            inner=[]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        ),
        ParsedRule(
            name='{self.rule}?',
            rule=Optional(
                rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586b1f0>,
                name='{self.rule}?'
            ),
            match='  ',
            span=(2, 4),
            parent=Optional(
                rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586b1f0>,
                name='{self.rule}?'
            ),
            inner=[
                ParsedRule(
                    name='whitespace',
                    rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586b1f0>,
                    match='  ',
                    span=(2, 4),
                    parent=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586b1f0>,
                    inner=[
                        ParsedRule(
                            name='<function rule at 0x7fda05a3f0a0>+',
                            rule=OnceOrMore(rule=' ', name='<function rule at 0x7fda05a3f0a0>+'),
                            match=' ',
                            span=(3, 4),
                            parent=OnceOrMore(rule=' ', name='<function rule at 0x7fda05a3f0a0>+'),
                            inner=[]
                        )
                    ]
                )
            ]
        ),
        ParsedRule(
            name='operator',
            rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586a800>,
            match='*',
            span=(4, 5),
            parent=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586a800>,
            inner=[
                ParsedRule(
                    name="'+'|'-'|'*'|'/'",
                    rule=<grap.core.rules.RuleUnion object at 0x7fda0586b400>,
                    match='*',
                    span=(4, 5),
                    parent=<grap.core.rules.RuleUnion object at 0x7fda0586b400>,
                    inner=[
                        ParsedRule(
                            name="'*'",
                            rule=<grap.core.rules.String object at 0x7fda0586a740>,
                            match='*',
                            span=(4, 5),
                            parent=<grap.core.rules.String object at 0x7fda0586a740>,
                            inner=[]
                        )
                    ]
                )
            ]
        ),
        ParsedRule(
            name='number',
            rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586b0d0>,
            match='420',
            span=(5, 8),
            parent=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586b0d0>,
            inner=[
                ParsedRule(
                    name='<function rule at 0x7fda05a3f0a0>+',
                    rule=OnceOrMore(
                        rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586b340>,
                        name='<function rule at 0x7fda05a3f0a0>+'
                    ),
                    match='420',
                    span=(5, 8),
                    parent=OnceOrMore(
                        rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586b340>,
                        name='<function rule at 0x7fda05a3f0a0>+'
                    ),
                    inner=[
                        ParsedRule(
                            name='digit',
                            rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586b340>,
                            match='4',
                            span=(5, 6),
                            parent=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586b340>,
                            inner=[
                                ParsedRule(
                                    name="'0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9'",
                                    rule=<grap.core.rules.RuleUnion object at 0x7fda0552ce80>,
                                    match='4',
                                    span=(5, 6),
                                    parent=<grap.core.rules.RuleUnion object at 0x7fda0552ce80>,
                                    inner=[
                                        ParsedRule(
                                            name="'4'",
                                            rule=<grap.core.rules.String object at 0x7fda0586b370>,
                                            match='4',
                                            span=(5, 6),
                                            parent=<grap.core.rules.String object at 0x7fda0586b370>,
                                            inner=[]
                                        )
                                    ]
                                )
                            ]
                        ),
                        ParsedRule(
                            name='digit',
                            rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586b340>,
                            match='2',
                            span=(6, 7),
                            parent=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586b340>,
                            inner=[
                                ParsedRule(
                                    name="'0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9'",
                                    rule=<grap.core.rules.RuleUnion object at 0x7fda0552d2a0>,
                                    match='2',
                                    span=(6, 7),
                                    parent=<grap.core.rules.RuleUnion object at 0x7fda0552d2a0>,
                                    inner=[
                                        ParsedRule(
                                            name="'2'",
                                            rule=<grap.core.rules.String object at 0x7fda0552cee0>,
                                            match='2',
                                            span=(6, 7),
                                            parent=<grap.core.rules.String object at 0x7fda0552cee0>,
                                            inner=[]
                                        )
                                    ]
                                )
                            ]
                        ),
                        ParsedRule(
                            name='digit',
                            rule=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586b340>,
                            match='0',
                            span=(7, 8),
                            parent=<grap.core.rules.rule.<locals>.decorator.<locals>.R object at 0x7fda0586b340>,
                            inner=[
                                ParsedRule(
                                    name="'0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9'",
                                    rule=<grap.core.rules.RuleUnion object at 0x7fda0552d6c0>,
                                    match='0',
                                    span=(7, 8),
                                    parent=<grap.core.rules.RuleUnion object at 0x7fda0552d6c0>,
                                    inner=[
                                        ParsedRule(
                                            name="'0'",
                                            rule=<grap.core.rules.String object at 0x7fda0552d3c0>,
                                            match='0',
                                            span=(7, 8),
                                            parent=<grap.core.rules.String object at 0x7fda0552d3c0>,
                                            inner=[]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)
