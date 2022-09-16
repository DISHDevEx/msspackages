from setuptools import find_packages, setup

setup(
    name='msspackages',
    version='0.0.3',    
    description='MSS team packages for distributed use',
    url='https://gitlab.global.dish.com/MSS/msspackages',
    include_package_data=True,
    author= 'Hamza Khokhar, Pierce Lovesee',
    author_email='hamza.khokhar@dish.com, pierce.lovesee@dish.com',
    license='',
    packages=find_packages(include=['msspackages', 'msspackages.extras', 'msspackages.circles',
                                    'msspackages.parity','msspackages.bucketization', 'msspackages.update_cwd']),
    
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: MSS Team',
    ],
)