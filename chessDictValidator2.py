# This program runs several checks to validate if the provided chess board is 
# valid. Each check is a function.
# Several incorrect boards have been created, to test the functionality of each
# helper function.

# valid board
playerDic = {'8a': 'brook', '8b': 'bknight', '8c': 'bbishop', '8d': 'bking', 
    '8e': 'bqueen', '8f': 'bbishop', '8g': 'bknight', '8h': 'brook', '7a': 'bpawn', 
    '7b': 'bpawn', '7c': 'bpawn', '7d': 'bpawn', '7e': 'bpawn', '7f': 'bpawn', 
    '7g': 'bpawn', '7h': 'bpawn', '1a': 'wrook', '1b': 'wknight', '1c': 'wbishop', '1d': 'wking', 
    '1e': 'wqueen', '1f': 'wbishop', '1g': 'wknight', '1h': 'wrook', '2a': 'wpawn', 
    '2b': 'wpawn', '2c': 'wpawn', '2d': 'wpawn', '2e': 'wpawn', '2f': 'wpawn', 
    '2g': 'wpawn', '2h': 'wpawn'}

# invalid board for test
playerDicMissingKing = {'8a': 'brook', '8b': 'bknight', '8c': 'bbishop', 
    '8e': 'bqueen', '8f': 'bbishop', '8g': 'bknight', '8h': 'brook', '7a': 'bpawn', 
    '7b': 'bpawn', '7c': 'bpawn', '7d': 'bpawn', '7e': 'bpawn', '7f': 'bpawn', 
    '7g': 'bpawn', '7h': 'bpawn', '1a': 'wrook', '1b': 'wknight', '1c': 'wbishop', '1d': 'wking', 
    '1e': 'wqueen', '1f': 'wbishop', '1g': 'wknight', '1h': 'wrook', '2a': 'wpawn', 
    '2b': 'wpawn', '2c': 'wpawn', '2d': 'wpawn', '2e': 'wpawn', '2f': 'wpawn', 
    '2g': 'wpawn', '2h': 'wpawn'}

# invalid board for test
playerDicExtraKing = {'8a': 'brook', '8b': 'bknight', '8c': 'bbishop', '8d': 'bking', 
    '8e': 'bqueen', '8f': 'bbishop', '8g': 'bknight', '8h': 'brook', '7a': 'bpawn', 
    '7b': 'bpawn', '7c': 'bpawn', '7d': 'bpawn', '7e': 'bpawn', '7f': 'bpawn', 
    '7g': 'bpawn', '7h': 'bpawn', '1a': 'wrook', '1b': 'wknight', '1c': 'wbishop', '1d': 'wking', 
    '1e': 'wqueen', '1f': 'wbishop', '1g': 'wknight', '1h': 'wrook', '2a': 'wpawn', 
    '2b': 'wpawn', '2c': 'wpawn', '2d': 'wpawn', '2e': 'wpawn', '2f': 'wpawn', 
    '2g': 'wpawn', '2h': 'wpawn', '4a': 'bking'}

# invalid board for test
playerDicExtraPieces = {'8a': 'brook', '8b': 'bknight', '8c': 'bbishop', '8d': 'bking', 
    '8e': 'bqueen', '8f': 'bbishop', '8g': 'bknight', '8h': 'brook', '7a': 'bpawn', 
    '7b': 'bpawn', '7c': 'bpawn', '7d': 'bpawn', '7e': 'bpawn', '7f': 'bpawn', 
    '7g': 'bpawn', '7h': 'bpawn', '1a': 'wrook', '1b': 'wknight', '1c': 'wbishop', '1d': 'wking', 
    '1e': 'wqueen', '1f': 'wbishop', '1g': 'wknight', '1h': 'wrook', '2a': 'wpawn', 
    '2b': 'wpawn', '2c': 'wpawn', '2d': 'wpawn', '2e': 'wpawn', '2f': 'wpawn', 
    '2g': 'wpawn', '2h': 'wpawn', '3h': 'wrook'}

# invalid board for test
playerDicExtraPawns = {'8a': 'brook', '8b': 'bknight', '8c': 'bbishop', '8d': 'bking', 
    '8e': 'bqueen', '8f': 'bbishop', '8g': 'bknight', '8h': 'brook', '7a': 'bpawn', 
    '7b': 'bpawn', '7c': 'bpawn', '7d': 'bpawn', '7e': 'bpawn', '7f': 'bpawn', 
    '7g': 'bpawn', '7h': 'bpawn', '1a': 'wrook', '1b': 'wknight', '1c': 'wbishop', '1d': 'wking', 
    '1e': 'wqueen', '1f': 'wbishop', '1g': 'wknight', '1h': 'wrook', '2a': 'wpawn', 
    '2b': 'wpawn', '2c': 'wpawn', '2d': 'wpawn', '2e': 'wpawn', '2f': 'wpawn', 
    '2g': 'wpawn', '2h': 'wpawn', '3h': 'wpawn'}

# invalid board for test
playerDicInvalidSpace = {'8a': 'brook', '8b': 'bknight', '8c': 'bbishop', '8d': 'bking', 
    '8e': 'bqueen', '8f': 'bbishop', '8g': 'bknight', '8h': 'brook', '7a': 'bpawn', 
    '7b': 'bpawn', '7c': 'bpawn', '7d': 'bpawn', '7e': 'bpawn', '7f': 'bpawn', 
    '7g': 'bpawn', '7h': 'bpawn', '1a': 'wrook', '1b': 'wknight', '1c': 'wbishop', '1d': 'wking', 
    '1e': 'wqueen', '1f': 'wbishop', '1g': 'wknight', '1h': 'wrook', '2a': 'wpawn', 
    '2b': 'wpawn', '2c': 'wpawn', '2d': 'wpawn', '2e': 'wpawn', '2f': 'wpawn', 
    '2g': 'wpawn', '2h': 'wpawn', '3z': 'bishop'}

# invalid board for test
playerDicInproperName = {'8a': 'brook', '8b': 'bknight', '8c': 'bbishop', '8d': 'bking', 
    '8e': 'bqueen', '8f': 'bbishop', '8g': 'bknight', '8h': 'brook', '7a': 'bpawn', 
    '7b': 'bpawn', '7c': 'bpawn', '7d': 'bpawn', '7e': 'bpawn', '7f': 'bpawn', 
    '7g': 'bpawn', '7h': 'bpawn', '1a': 'wrook', '1b': 'wknight', '1c': 'wbishop', '1d': 'wking', 
    '1e': 'wqueen', '1f': 'wbishop', '1g': 'wknight', '1h': 'wrook', '2a': 'wpawn', 
    '2b': 'wpawn', '2c': 'wpawn', '2d': 'wpawn', '2e': 'wpawn', '2f': 'wpawn', 
    '2g': 'wpawn', '2h': 'wpanw'}

boards = [playerDic, playerDicExtraKing, playerDicExtraPawns, playerDicExtraPieces, 
playerDicMissingKing, playerDicInproperName, playerDicInvalidSpace]

# --- Check 1: King Count ---
def check_king_counts(boardDic):
    """Checks there is exactly 1 white and 1 black king."""
    whiteKingCount = 0
    blackKingCount = 0

    for k, v in boardDic.items():
        if v == 'wking':
            whiteKingCount += 1
        elif v == 'bking':
            blackKingCount += 1
    # There can be only 1 white and black king
    if whiteKingCount == 1 and blackKingCount == 1:
         return True
    else:
         return False

# --- Check 2: Total Piece Count ---
def check_piece_count(boardDic):
    """Check there are 16 pieces in total for each player."""
    white_piece_count = 0
    black_piece_count = 0

    for v in boardDic.values():
        if v.startswith('w'):
            white_piece_count += 1
        elif v.startswith('b'):
            black_piece_count += 1
    # 16 total pieces per player
    if white_piece_count <= 16 and black_piece_count <= 16:
        return True
    else:
        return False

 # --- Check 3: Pawn Count ---
def check_pawn_count(boardDic):
    """Check there are exactly 8 pawns for each player."""
    white_pawn_count = 0
    black_pawn_count = 0

    for k, v in boardDic.items():
        if 'pawn' in v and v.startswith('w'):
            white_pawn_count += 1
        elif 'pawn' in v and v.startswith('b'):
            black_pawn_count += 1
    # 8 pawns per player
    if white_pawn_count <= 8 and black_pawn_count <= 8:
        return True
    else:
        return False

# --- Check 4: Validate Spaces ---
def check_valid_spaces(boardDic):
    """Check the piece spaces are valid."""
    valid_rank = '12345678'
    valid_file = 'abcdefgh'

    for k, v in boardDic.items():
        # check length is 2
        if not len(k) == 2:
            return False

        # check 1st character is a digit and 2nd is a letter
        if not (k[0].isdigit() and k[1].isalpha()):
            return False
        # check 1st and 2nd character's are valid
        if not (k[0] in valid_rank and k[1] in valid_file):
            return False

    return True

# --- Check 5: Validate Piece Names ---
def check_piece_name(boardDic):
    """Check the piece names are valid."""
    valid_piece_types = {'pawn', 'rook', 'bishop', 'knight', 'king', 'queen'}

    for k, v in boardDic.items():
        # If the piece name DOES NOT start with 'w' AND DOES NOT start with 'b'
        if not (v.startswith('w') or v.startswith('b')):
            return False
        # check rest of piece name is valid
        piece_type = v[1:]
        if not piece_type in valid_piece_types:
            return False

    # Check all pieces before returning True  
    return True

# ---Main Validation Function---    
def isValidChessBoard(boardDic):
    """Pulls the individual check helper functions together."""
    # if not negates result of check so the main check run the next helper func
    if not check_king_counts(boardDic):
        return False
    if not check_piece_count(boardDic):
        return False
    if not check_pawn_count(boardDic):
        return False
    if not check_piece_name(boardDic):
        return False
    if not check_valid_spaces(boardDic):
        return False

    return True

# ---Test the function---
# print(isValidChessBoard(playerDic))

# ---Test the function on all boards---
print('\nTesting all boards...')
for board in boards:
    print(isValidChessBoard(board))







    



