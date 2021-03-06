class FontColors:
    RED: str = '\033[31m'
    GREEN: str = '\033[32m'
    YELLOW: str = '\033[33m'
    RESET: str = '\033[0m'


ERROR_INVALID_SOURCE_NAME: str = FontColors.RED + \
    'Cannot record such source name. Try again.' + FontColors.RESET

ERROR_ASR_SERVER_NOT_STARTED: str = FontColors.RED + \
    'ASR-server is not started.' + FontColors.RESET

RECORDING_HELP_MSG: str = 'Press enter to start recording.' + \
    '\n' + \
    'Enter the <q> key to quit.'

WS_ON_OPEN: str = 'Wessocket connected'

WS_ON_CLOSE: str = 'Wessocket closed'


def WS_ON_MESSAGE(message: str) -> str:
    result: str = 'Wessocket receive ' + \
        FontColors.GREEN + message + FontColors.RESET
    return result


def WS_ON_ERROR(message: str) -> str:
    result: str = 'Wessocket error ' + \
        FontColors.RED + message + FontColors.RESET
    return result


def WS_SEND_MSG(message: str) -> str:
    result: str = 'Wessocket send ' + \
        FontColors.GREEN + message + FontColors.RESET
    return result


def CREATED_FILE_MSG(file_name: str) -> str:
    result: str = 'Created ' + FontColors.YELLOW + file_name + FontColors.RESET
    return result


def DELETE_FILE_MSG(file_name: str) -> str:
    result: str = 'Deleted ' + FontColors.YELLOW + file_name + FontColors.RESET
    return result


def PLAY_AUDIO_MSG(text: str) -> str:
    result: str = 'Play ' + FontColors.YELLOW + text + FontColors.RESET
    return result
