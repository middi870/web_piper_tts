# Piper TTS Voice Models - Complete List

This document contains all available Piper TTS voice models organized by language.
Each voice comes in different quality levels: x_low, low, medium, and high.

## English (United States) - en_US

### Female Voices
- **Amy** - Low, Medium
- **HFC_Female** - Medium
- **Kathleen** - Low
- **Kristin** - Medium
- **Ljspeech** - Medium, High

### Male Voices
- **Arctic** - Medium (Multi-speaker, 18 speakers)
- **Bryce** - Medium
- **Danny** - Low
- **HFC_Male** - Medium
- **Joe** - Medium
- **John** - Medium
- **Kusal** - Medium
- **Lessac** - Low, Medium, High
- **Norman** - Medium
- **Ryan** - Low, Medium, High

### Multi-Speaker
- **L2arctic** - Medium (Multi-speaker)
- **Libritts** - High (Multi-speaker, 904 speakers)
- **Libritts_R** - Medium (Multi-speaker, 904 speakers)

## English (British) - en_GB

### Female Voices
- **Alba** - Medium
- **Cori** - Medium, High
- **Jenny_Dioco** - Medium
- **Southern_English_Female** - Low

### Male Voices
- **Alan** - Low, Medium
- **Aru** - Medium
- **Northern_English_Male** - Medium
- **Semaine** - Medium (Multi-speaker, 4 speakers)

### Multi-Speaker
- **Vctk** - Medium (Multi-speaker, 109 speakers)

## Spanish (Spain) - es_ES

- **Carlfm** - X_Low (Male)
- **Davefx** - Medium (Male)
- **Mls_10246** - Low (Female)
- **Mls_9972** - Low (Male)
- **Sharvard** - Medium (Male)

## Spanish (Mexico) - es_MX

- **Ald** - Medium (Male)
- **Claude** - High (Female)

## French (France) - fr_FR

- **Gilles** - Low (Male)
- **Mls** - Medium (Multi-speaker)
- **Mls_1840** - Low (Female)
- **Siwis** - Low, Medium (Female)
- **Tom** - Medium (Male)
- **Upmc** - Medium (Multi-speaker, 2 speakers)

## German (Germany) - de_DE

- **Eva_K** - X_Low (Female)
- **Karlsson** - Low (Male)
- **Kerstin** - Low (Female)
- **Mls** - Medium (Multi-speaker)
- **Pavoque** - Low (Male)
- **Ramona** - Low (Female)
- **Thorsten** - Low, Medium, High (Male)
- **Thorsten_Emotional** - Medium (Male, with emotions)

## Russian (Russia) - ru_RU

- **Denis** - Medium (Male)
- **Dmitri** - Medium (Male)
- **Irina** - Medium (Female)
- **Ruslan** - Medium (Male)

## Portuguese (Brazil) - pt_BR

- **Edresson** - Low (Male)
- **Faber** - Medium (Male)

## Portuguese (Portugal) - pt_PT

- **Tugao** - Medium (Male)

## Italian (Italy) - it_IT

- **Paola** - Medium (Female)
- **Riccardo** - X_Low (Male)

## Polish (Poland) - pl_PL

- **Darkman** - Medium (Male)
- **Gosia** - Medium (Female)
- **McSpeech** - Medium (Male)
- **Mls_6892** - Low (Male)

## Dutch (Netherlands) - nl_NL

- **Mls** - Medium (Multi-speaker)
- **Mls_5809** - Low (Female)
- **Mls_7432** - Low (Male)

## Dutch (Belgium) - nl_BE

- **Nathalie** - Low, Medium (Female)
- **Rdh** - X_Low, Medium (Male)

## Turkish (Turkey) - tr_TR

- **Dfki** - Medium (Male)
- **Fahrettin** - Medium (Male)
- **Fettah** - Medium (Male)

## Ukrainian (Ukraine) - uk_UA

- **Lada** - X_Low (Female)
- **Ukrainian_TTS** - Medium (Multi-speaker)

## Czech (Czech Republic) - cs_CZ

- **Jirka** - Low, Medium (Male)

## Catalan (Spain) - ca_ES

- **UPC_Ona** - X_Low, Medium (Female)
- **UPC_Pau** - X_Low (Male)

## Hungarian (Hungary) - hu_HU

- **Anna** - Medium (Female)
- **Berta** - Medium (Female)
- **Imre** - Medium (Male)

## Icelandic (Iceland) - is_IS

- **Bui** - Medium (Male)
- **Salka** - Medium (Female)
- **Steinn** - Medium (Male)
- **Ugla** - Medium (Female)

## Danish (Denmark) - da_DK

- **Talesyntese** - Medium

## Greek (Greece) - el_GR

- **Rapunzelina** - Low (Female)

## Persian (Iran) - fa_IR

- **Amir** - Medium (Male)
- **Gyro** - Medium (Male)

## Finnish (Finland) - fi_FI

- **Harri** - Low (Male)

## Georgian (Georgia) - ka_GE

- **Natia** - Medium (Female)

## Kazakh (Kazakhstan) - kk_KZ

- **Iseke** - X_Low (Male)
- **Issai** - High (Male)
- **Raya** - X_Low (Female)

## Luxembourgish (Luxembourg) - lb_LU

- **Marylux** - Medium (Female)

## Latvian (Latvia) - lv_LV

- **Aivars** - Medium (Male)

## Nepali (Nepal) - ne_NP

- **Google** - X_Low, Medium

## Norwegian (Norway) - no_NO

- **Talesyntese** - Medium

## Romanian (Romania) - ro_RO

- **Mihai** - Medium (Male)

## Slovak (Slovakia) - sk_SK

- **Lili** - Medium (Female)

## Slovenian (Slovenia) - sl_SI

- **Artur** - Medium (Male)

## Serbian (Serbia) - sr_RS

- **Serbski_Institut** - Medium

## Swedish (Sweden) - sv_SE

- **NST** - Medium (Multi-speaker)

## Swahili (DR Congo) - sw_CD

- **Lanfrica** - Medium

## Vietnamese (Vietnam) - vi_VN

- **25hours_single** - Low
- **Vais1000** - Medium
- **Vivos** - X_Low

## Welsh (United Kingdom) - cy_GB

- **Gwryw_Gogleddol** - Medium (Male)

---

## Quality Levels Explained

- **x_low** - Fastest, smallest file size, lower quality
- **low** - Fast, small file size, decent quality
- **medium** - Balanced speed and quality (recommended)
- **high** - Slower, larger file size, best quality

## How to Use in Python

```python
# Example voice model names for use in scripts:
"en_US-amy-low"
"en_US-ryan-medium"
"en_GB-alan-medium"
"es_ES-davefx-medium"
"fr_FR-tom-medium"
"de_DE-thorsten-medium"
"ru_RU-dmitri-medium"

# Format: {language_code}-{voice_name}-{quality}
```

## Popular Recommendations

### Best Quality English Voices
1. **en_US-lessac-high** - High quality, clear
2. **en_US-ryan-high** - Natural male voice
3. **en_US-ljspeech-high** - Clear female voice
4. **en_GB-cori-high** - British English

### Fastest English Voices
1. **en_US-amy-low** - Quick, female
2. **en_US-danny-low** - Quick, male
3. **en_GB-alan-low** - Quick, British male

### Emotional/Expressive
1. **de_DE-thorsten_emotional-medium** - German with emotions
2. **en_US-arctic-medium** - Multi-speaker with variation

### Multi-Speaker Models (Multiple voices in one model)
1. **en_US-libritts-high** - 904 different speakers!
2. **en_GB-vctk-medium** - 109 different speakers
3. **en_US-arctic-medium** - 18 different speakers

---

Total Languages: 40+
Total Voices: 200+
