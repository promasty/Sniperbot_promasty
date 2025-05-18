def verify_metadata(token):
    # Simulace kontroly webu a Twitteru (můžeš přidat reálnou kontrolu)
    if 'website' in token and 'twitter' in token:
        return True
    return False