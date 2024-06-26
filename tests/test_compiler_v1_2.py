# Usage: niwatoko [OPTIONS] [FILE_PATH]

#   自然言語のソースコードを読み込んで実行するコマンドラインインターフェース。

#   Args:     file_path (str): 自然言語のソースコードが書かれたファイルのパス。     model (str):
#   使用するモデル（OpenAIまたはClaude）。     output (str): 生成されたコードの出力先ファイルのパス。     version
#   (bool): バージョン情報を表示するかどうか。

# Options:
#   -m, --model [openai|claude]  使用するモデルを選択します。
#   -o, --output PATH            生成されたコードの出力先ファイルを指定します。
#   -v, --version                バージョン情報を表示します。
#   --help                       Show this message and exit.


import subprocess
import os
from click.testing import CliRunner
from niwatoko.cli import main

# テストケースを関数として定義する
def test_version():
    """
    バージョン情報が正しく表示されることを確認するテストケース
    """
    runner = CliRunner()
    result = runner.invoke(main, ['--version'])
    assert result.exit_code == 0
    assert 'niwatoko version:' in result.output

def test_no_file_path():
    """
    ファイルパスが指定されていない場合のエラーメッセージを確認するテストケース
    """
    runner = CliRunner()
    result = runner.invoke(main, [])
    assert result.exit_code == 0
    assert 'ファイルパスが指定されていません。' in result.output

def test_invalid_model():
    """
    無効なモデルが指定された場合のエラーを確認するテストケース
    """
    runner = CliRunner()                                                      # CLIRunnerオブジェクトを作成
    result = runner.invoke(main, ['sample.md', '--model', 'invalid'])         # mainコマンドを'sample.md'ファイルと'invalid'モデルオプションで実行
    assert result.exit_code == 2                                              # - 実行結果のexitコードが1であることを確認
    assert 'Error: Invalid value for' in result.output              # - 出力にエラーメッセージが含まれていることを確認

def test_generate_response_claude(tmp_path):
    """
    Claudeモデルを使用して自然言語コードから生成されたコードを確認するテストケース
    """
    sample_file = tmp_path / 'sample.md'
    sample_file.write_text('自然言語のコードサンプル')
    output_file = tmp_path / 'output.py'

    runner = CliRunner()
    result = runner.invoke(main, [str(sample_file), '--model', 'claude', '--output', str(output_file)])
    assert result.exit_code == 0
    assert os.path.exists(output_file)
    assert 'に書き出しました。' in result.output

def test_generate_response_openai(tmp_path):
    """
    OpenAIモデルを使用して自然言語コードから生成されたコードを確認するテストケース
    """
    sample_file = tmp_path / 'sample.md'
    sample_file.write_text('自然言語のコードサンプル')
    output_file = tmp_path / 'output.py'

    runner = CliRunner()
    result = runner.invoke(main, [str(sample_file), '--model', 'openai', '--output', str(output_file)])
    assert result.exit_code == 0
    assert os.path.exists(output_file)
    assert 'に書き出しました。' in result.output
# ```

# 解説
# このコードは、`niwatoko`パッケージの`cli`モジュールをテストするための`pytest`テストケースを定義しています。

# - `test_version`関数は、`--version`オプションが正しく動作することを確認します。
# - `test_no_file_path`関数は、ファイルパスが指定されていない場合に適切なエラーメッセージが表示されることを確認します。
# - `test_invalid_model`関数は、無効なモデルが指定された場合に適切なエラーメッセージが表示されることを確認します。
# - `test_generate_response_claude`関数は、Claudeモデルを使用して自然言語コードから生成されたコードが正しく出力されることを確認します。
# - `test_generate_response_openai`関数は、OpenAIモデルを使用して自然言語コードから生成されたコードが正しく出力されることを確認します。

# これらのテストケースは、`click.testing.CliRunner`を使用して`niwatoko.cli.main`関数をテストしています。一時ディレクトリを作成し、そこにサンプルファイルと出力ファイルを作成して、CLIの動作を確認しています。

# このテストコードを実行することで、CLIの機能が正しく動作することを確認できます。また、将来的な機能追加や修正の際にも、回帰テストとして活用できます。
