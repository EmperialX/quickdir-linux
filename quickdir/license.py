licenses = {
    'MIT': {
        'name': 'MIT License',
        'url': 'https://opensource.org/licenses/MIT',
        'header': 'MIT License\n\n'
    },
    'Apache': {
        'name': 'Apache License 2.0',
        'url': 'https://www.apache.org/licenses/LICENSE-2.0',
        'header': 'Apache License\nVersion 2.0, January 2004\n\n'
    },
    'GPL': {
        'name': 'GNU General Public License v3.0',
        'url': 'https://www.gnu.org/licenses/gpl-3.0.en.html',
        'header': 'GNU GENERAL PUBLIC LICENSE\nVersion 3, 29 June 2007\n\n'
    }
}

def get_license_header(license_name):
    if license_name not in licenses:
        raise ValueError(f'Invalid license name "{license_name}"')

    return licenses[license_name]['header']
