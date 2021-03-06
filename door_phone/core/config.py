# path config
DATA_ROOT_PATH: str = './data'
RECORD_WAV_PATH: str = DATA_ROOT_PATH + '/record.wav'
UPLOAD_WAV_PATH: str = DATA_ROOT_PATH + '/upload.wav'

# wave config
WAVE_RATE: int = 16000
WAVE_WIDTH: int = 2
WAVE_CHANNELS: int = 1
WAVE_CHUNK: int = 1024
WAVE_DEFECT_SEC: float = 0.4
WAVE_AMP_SAMPLES: int = 6

# wave preprocessing config
BPF_LOW_FREQ: int = 100
BPF_HIGH_FREQ: int = 8000

# api config
ASR_URL: str = 'https://hack.abelab.dev/predict'
ASR_NUMBER_URL: str = ASR_URL + '/' + 'number'
ASR_TEXT_URL: str = ASR_URL + '/' + 'text'
DOCOMO_URL: str = \
    'https://api.apigw.smt.docomo.ne.jp/futureVoiceCrayon/v1/textToSpeech?APIKEY='
DOCOMO_COMMAND: str = 'AP_Synth'
DOCOMO_SPEAKER_ID: str = '2'
DOCOMO_STYLE_ID: str = DOCOMO_SPEAKER_ID
DOCOMO_SPEECH_RATE: str = '1.15'
DOCOMO_AUDIO_FILE_FORMAT: str = '2'
INTERMEDIATE_SERVER_URL: str = 'ws://hack.inatatsu.com:8000/'
