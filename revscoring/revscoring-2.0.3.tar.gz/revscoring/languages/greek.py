from .features import Dictionary, RegexMatches, Stopwords

name = "greek"

try:
    import enchant
    dictionary = enchant.Dict("el")
except enchant.errors.DictNotFoundError:
    raise ImportError("No enchant-compatible dictionary found for 'el'.  " +
                      "Consider installing 'aspell-el'.")

dictionary = Dictionary(name + ".dictionary", dictionary.check)
"""
:class:`~revscoring.languages.features.Dictionary` features via
:class:`enchant.Dict` "el". Provided by `aspell-el`.
"""

stopwords = [
    "αλλά", "άλλα", "άν", "αντί", "από", "αυτά", "αυτές", "αυτή", "αυτό",
    "αυτοί", "αυτός", "αυτούς", "αυτών", "για", "δε", "δεν", "δι'", "διά",
    "εάν", "είμαι", "είμαστε", "είναι", "είσαι", "είστε", "εκείνα",
    "εκείνες", "εκείνη", "εκείνο", "εκείνοι", "εκείνος", "εκείνους",
    "εκείνων", "ενώ", "επι", "η", "ή", "θα", "ισως", "κατ", "κατά",
    "μήτε", "μα", "με", "μετά", "μη", "μην", "μεν", "να", "ο", "οι",
    "όμως", "όπως", "όσο", "ότι", "οι", "παρ", "παρά", "παρα", "περί",
    "ποια", "ποιες", "ποιο", "ποιοι", "ποιος", "ποιους", "ποιων",
    "πότε", "που", "πού", "προ", "προς", "πώς", "πως", "σε", "στη",
    "στην", "στο", "στον", "τα", "την", "τι", "τινα", "τις", "το",
    "τον", "τότε", "του", "τούς", "των", "ως", "ώστε"
]

stopwords = Stopwords(name + ".stopwords", stopwords)
"""
:class:`~revscoring.languages.features.Stopwords` features copied from
"common words" in
"""

badword_regexes = [
    r"αδε(ρ|λ)φ[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"αλ(ή|η)τ[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"(α|ά)χρηστ[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"αρχ(ί|ι)δ[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"(αντι)?(νεο)?φιλελ(ε|έ)(ς|δες)?",
    r"βλ(α|ά)κ[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"β(ύ|υ)ζ(?!(α|ά)ν)[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"γαμ(ω|ώ)",
    r"γαμι(έ|ε)[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"γαμημ(έ|ε)ν(ος|η|ο|α|ων|ου)",
    r"γαμι(ά|α)ς",
    r"γκ(έ|ε)ι",
    r"γαμ(ώ|ω)το",
    r"γ(ύ|υ)φτ[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"δι(ά|α)ολ[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"ελαφροχέρ[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"ηλ(ι|ί)θ[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"(γ)?κ(ά|α)(β|υ|ύ)λ[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"κουρ(ά|α)δ[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"κομμουνιστοσυμμορ(ί|ι)τ[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"κ(ώ|ω|ό|ο)λ[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"κουτ(ό|ο)(ς)?",
    r"κουφ(ά|α)λα",
    r"κλ(ά|α)ν[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"κ(ά|α)ρι(ό|ο)λ[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"κλ(έ|ε)φτ[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"λεσβ(ί|ι)α",
    r"λο(ύ|υ)γκρ[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"μο(ύ|υ)ν[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"μπ(ά|α)στ(ά|α)ρδ[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"μαλ(ά|α)κ[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"ντα(ή|η)[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"ντουγ(ά|α)ν[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"ξεδι(ά|α)ντρ[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"ξετσ(ί|ι)πωτ[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"πουτ(ά|α)ν[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"πο(ύ|υ)στ[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"πεισματ(ά|α)ρ[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"φ(ύ|υ)τουλ[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"ρουφι(ά|α)ν[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
]

badwords = RegexMatches(name + ".badwords", badword_regexes)
"""
:class:`~revscoring.languages.features.RegexMatches` features via a list of
badword detecting regexes.
"""

informal_regexes = [
    r"άντε",
    r"άσε",
    r"άστ(ο|η|α)",
    r"ε(σ|μ)(ά|α)ς",
    r"(μ|σ)ας",
    r"γεια",
    r"μπαι",
    r"τραν(σ|ς)[α-ωΑ-Ωάέήίόύώϊΐϋΰ]*",
    r"φίλε",
    r"μαν",
    r"(μπλα)+",
    r"(χα)+",
    r"(χε)+",
    r"(χι)+",
    r"(χο)+"
]

informals = RegexMatches(name + ".informals", informal_regexes)
"""
:class:`~revscoring.languages.features.RegexMatches` features via a list of
informal word detecting regexes.
"""
