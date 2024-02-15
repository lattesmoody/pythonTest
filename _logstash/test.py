filter {
  ruby {
    code => "
      require 'open3'

      def convert_cp949_to_utf8(cp949_string)
        # Python 스크립트 실행
        stdin, stdout, stderr = Open3.popen3('python3 -c \"import sys; print(sys.argv[1].encode(\'cp949\').decode(\'utf-8\'))\"', :stdin_data => cp949_string)
        stdout.read.strip
      end

      event.set('your_field_name', convert_cp949_to_utf8(event.get('your_field_name')))
    "
  }
}