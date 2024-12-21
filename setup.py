from setuptools import setup, Extension, find_packages

with open("README.md", "r") as fh:
    readme = fh.read()

with open("requirements.txt", "r") as req:
    requirements = req.read()

setup(
    name = 'soundtrack',
    version = '0.0.0.0',
    url = 'https://github.com/hbisneto/SoundTrack',
    license = 'MIT License',
    
    author = 'Heitor Bisneto',
    author_email = 'heitor.bardemaker@live.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    description = u'SoundTrack is a powerful Python library designed to simplify audio processing tasks, specifically focusing on separating various audio tracks such as vocals, bass, and drums from music files. Leveraging advanced AI models like Demucs, SoundTrack offers a straightforward way to isolate different elements of a song with high precision.',
    install_requires = requirements,
    long_description = readme,
    long_description_content_type = "text/markdown",
    keywords = ['SoundTrack', 'Music', 
                'Vocals', 'Drums', 
                'Bass', 'Separate', 
                'Extract', 'Demucs', 
            ],
    packages=find_packages(),
    platforms = 'any',
    python_requires= '>=3.8',
)